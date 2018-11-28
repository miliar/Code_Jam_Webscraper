#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<queue>
#include<fstream>
#include<cmath>
using namespace std;
long long t,l,x;
string s;
long long m[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int main()
{
	ifstream cin;
	cin.open("C-small-attempt1.in");
	freopen("output.txt","w",stdout);
	cin>>t;
	for(int o=1; o<=t; o++)
	{
		cin>>l>>x;
		cin>>s;
		string ds=s+s+s+s+s+s+s+s+s;
		int p=s[0]-'i'+2,e=0,pos=0;
		if(p==2) {pos=1; e=1;}
		else
            for(int i=1; i<=4*l-1; i++)
            {
                if(p<0) {p=-m[-p][ds[i]-'i'+2];}
                else p=m[p][ds[i]-'i'+2];
                if(p==2) {pos=i+1; e=1; break;}
            }
        if(e==0) {printf("Case #%d: NO\n",o); continue;}
        //ds=ds+s+s;
        p=ds[pos]-'i'+2;
        e=0;
        if(p==3) {pos+=1; e=1;}
        else
            for(int i=pos+1; i<=4*l+pos-1; i++)
            {
                if(p<0) {p=-m[-p][ds[i]-'i'+2];}
                else p=m[p][ds[i]-'i'+2];
                if(p==3) {pos=i+1; e=1; break;}
            }
        if(e==0) {printf("Case #%d: NO\n",o); continue;}
        int k=pos/l+1;
        if(k>x) {printf("Case #%d: NO\n",o); continue;}
        k=x-k;
        if(pos%l==0) {p=1; k++;}
        else
        {
            p=ds[pos]-'i'+2; pos++;
            while(pos%l!=0)
            {
                if(p<0) {p=-m[-p][ds[pos]-'i'+2];}
                else p=m[p][ds[pos]-'i'+2];
                pos++;
            }
        }
        int op=s[0]-'i'+2;
        for(int i=1; i<=l-1; i++)
        {
            if(op<0) {op=-m[-op][s[i]-'i'+2];}
            else op=m[op][s[i]-'i'+2];
        }
        int res[4];
        res[1]=op;
        for(int i=2; i<=4; i++)
        {
            if(res[i-1]<0)
            {
                if(op<0) res[i%4]=m[-res[i-1]][-op];
                else res[i%4]=-m[-res[i-1]][op];
            }
            else
            {
                if(op<0) res[i%4]=-m[res[i-1]][-op];
                else res[i%4]=m[res[i-1]][op];
            }
        }
        int ansp=0;
        if(p<0)
        {
            if(res[k%4]<0) ansp=m[-p][-res[k%4]];
            else ansp=-m[-p][res[k%4]];
        }
        else
        {
            if(res[k%4]<0) ansp=-m[p][-res[k%4]];
            else ansp=m[p][res[k%4]];
        }
        if(ansp==4) printf("Case #%d: YES\n",o);
        else printf("Case #%d: NO\n",o);
	}
	cin.close();
	return 0;
}
