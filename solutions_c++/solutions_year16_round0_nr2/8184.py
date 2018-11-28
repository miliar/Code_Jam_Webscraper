#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
	int t;
	//scanf("%d",&t);
	int X=0;
	ifstream f1;
    ofstream f2;
    f1.open("B-large.in");
    f2.open("output.out");
	f1>>t;
	while(t--)
	{

        string s1,s2;
        f1>>s1;
        //cout<<s1;
        s2=s1;
        bool b=true; ll count=0,count1=0;
        int n=s1.length();
        while(b)
        {
            int i=0;
            for(;i<n;i++) if(s1[i] == '-') break;
            if(i==n) break;
            int z=n-1;
            while(s1[z] != '-' && z>= 0)
            {
                z--;
            }
            //if(z == 1) {count=2;break;}
            for(int j=0;j<=z/2;j++)
            {
                swap(s1[j],s1[z-j]);
            }
            for(int j=0;j<=z;j++)
            {
                if(s1[j] == '+') s1[j] ='-';
                else s1[j]='+';
            }
            //b=false;
            count++;
            i=0;
            for(;i<n;i++) if(s1[i] == '-') break;
            if(i==n) break;
            z=0;
            while(s1[z+1] != '-')
            {
                z++;
            }

            for(int j=0;j<=z;j++)
            {
                 s1[j] ='-';
               //s1[j]='+';
            }
            count++;
            //cout<<s1<<" ";
        }

        b=true;
        while(b)
        {
            int i=0;
            for(;i<n;i++) if(s2[i] == '-') break;
            if(i==n) break;
            int z=0;
            while(s2[z] != '-')
            {
                z++;
            }
			z--;
            for(int j=0;j<=z;j++)
            {
                 s2[j] ='-';
               //s1[j]='+';
            }
            count1++;
             i=0;
            for(;i<n;i++) if(s2[i] == '-') break;
            if(i==n) break;

            z=n-1;
            while(s2[z] != '-' && z>= 0)
            {
                z--;
            }
            //if(z == 1) {count=2;break;}
            for(int j=0;j<=z/2;j++)
            {
                swap(s2[j],s2[z-j]);
            }
            for(int j=0;j<=z;j++)
            {
                if(s2[j] == '+') s2[j] ='-';
                else s2[j]='+';
            }
            //b=false;
            count1++;

            //cout<<s2<<" ";
        }
X++;
        f2<<"Case #"<<X<<": "<<min(count,count1)<<"\n";

	}
	f1.close();
    f2.close();
	return 0;
}
