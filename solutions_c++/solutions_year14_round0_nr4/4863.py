#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <iostream>
#include <cstdio>

using namespace std;


int calculatedeceitfulWar(double naomi[], double ken[], int n)
{
    int i, j, kenn = 0 ;

    for(i=n, j=n; j>=1; i--,j--)
    {
        //cout<<naomi[i]<<", "<<ken[j]<<endl;
        if(naomi[i]<ken[j])
        {
            kenn++;
            i++;
        }

    }

    return n-kenn;
}


int calculateWar(double naomi[], double ken[], int n)
{
    int dead[n+1];
    int i, j;

    for(i=1; i<=n; i++)
    {
        for(j=1; j<=n; j++)
        {
            if((ken[j]>naomi[i])&&(dead[j]!=1))
            {
                dead[j] = 1;
                break;
            }
        }

        if(j==n+1)
            return n-i+1;
    }

    return 0;
}

int main(int argc, const char *argv[])
{
	string inputFileName = "D-small-attempt0.in";
	string outputFileName = "output.txt";
	freopen(inputFileName.c_str(), "r", stdin);
	freopen(outputFileName.c_str(), "w", stdout);

	int t, n, i, j, war, deceitfulWar;
	double naomi[1010], ken[1010];

	cin>>t;

	for(i=1; i<=t; i++)
	{
	    cin>>n;

	    for(j=1; j<=n; j++)
            cin>>naomi[j];

        for(j=1; j<=n; j++)
            cin>>ken[j];

        sort(naomi+1, naomi+n+1);
        sort(ken+1, ken+n+1);

        /*for(j=1; j<=n; j++)
            cout<<naomi[j]<<", ";
        cout<<endl;

        for(j=1; j<=n; j++)
            cout<<ken[j]<<", ";
        cout<<endl;*/

        war = calculateWar(naomi, ken, n);
        deceitfulWar = calculatedeceitfulWar(naomi, ken, n);
        //deceitfulWar = -1;

        cout<<"Case #"<<i<<": "<<deceitfulWar<<" "<<war<<endl;
	}

	return 0;
}
