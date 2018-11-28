#include <algorithm>
#include <iostream>
#include <cstdio>
using namespace std;
#define ES 1.0e-7

int unfair(float ken[], float naomi[], int n);

int fair(float ken[], float naomi[], int n);


int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int t;
    cin >> t;
    int X=1;
    while(X<=t)
    {   int n;
        cin>>n;
        float ken[n], naomi[n];
        for(int i=0; i<n; i++)
            cin >> naomi[i];
        for(int i=0; i<n; i++)
            cin >> ken[i];


        cout << "Case #"<< X <<": " << unfair(ken, naomi, n) << " " << fair(ken, naomi, n) << endl;

        X++;
    }
}


int unfair(float ken[], float naomi[], int n)
{
    int counter=0;
    sort(naomi, naomi+n);
    sort(ken, ken+n);
    reverse(naomi, naomi+n);
    reverse(ken, ken+n);

    for(int i=0,j=0; i<n;)
    {

        if(ken[i]-ES < naomi[j]-ES)
        {

            counter++;
            i++;j++;
        }
        else
        {
            i++;
        }
    }

    return counter;
}

int fair(float ken[], float naomi[], int n)
{
    int counter=0;
    sort(naomi, naomi+n);
    reverse(naomi, naomi+n);
    sort(ken, ken+n);
    reverse(ken, ken+n);
    for(int i=0, j=0; i<n;)
    {



        if(naomi[i]-ES < ken[j]-ES)
        {
            i++;j++;
        }
        else
        {


            i++;
            counter++;
        }
    }
    return counter;

}

