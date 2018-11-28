#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main(){
    ifstream cin("IN11l.in");
    ofstream cout("o11.txt");
	int t;
	cin>>t;
	for(int z=1;z<=t;z++){
		string s1;
		char s2[1000];
		cin>>s1;
		int n=s1.size(),n2=0,j=n2;
		for(int i=0;i<n;i++)
        {
            if(s1[i] >= s2[0] && i!=0)
            {
                j=n2-1;
                s2[n2]=s2[j];
                while(j>=0)
                {
                    s2[j]=s2[j-1];
                    j--;
                }
                s2[0]= s1[i];
            }
            else
            {
                s2[n2]=s1[i];
            }
            n2++;
        }
        cout<<"Case #"<<z<<": ";
        for(int i=0;i<n2;i++)
        {
            cout<<s2[i];
        }
        cout<<endl;
	}
	return 0;
}
