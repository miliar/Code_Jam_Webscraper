#include <iostream>
#include <vector>
#include<cstdlib>
#include <algorithm>
#include <fstream>

using namespace std;


int main()
{
    ifstream cin;
	ofstream cout;
	cin.open("A-large.in");
	cout.open("A-large-output.txt");
	int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int n,j,x;
        cin>>n;
        vector<long long> v;
        for(j=0;j<n;j++)
        {
            cin>>x;
            v.push_back(x);
        }

        long long result1=0,result2=0,temp=0;
        for(j=1;j<n;j++)
        {
            if(v[j]-v[j-1]<0)
            {
            	result1+=(v[j-1]-v[j]);
            }
            temp=max(temp,v[j-1]-v[j]);
        }
        
        for(j=0;j<n-1;j++)
        {
            if(v[j]>=temp)
            {
                result2+=temp;
            }
            else
            {
                result2+=v[j];
				//v[j+1]-=(v[j]-temp);
            }

        }
        cout<<"Case #"<<i<<": "<<result1<<" "<<result2<<endl;

    }
    return 0;
}

