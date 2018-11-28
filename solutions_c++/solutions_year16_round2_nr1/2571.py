#include<bits/stdc++.h>
#define ll   long long

#define md 1000000007

using namespace std;
int h[30];
int ans[10];
int main()
{
	ios_base::sync_with_stdio(0);
   #ifndef ONLINE_JUDGE
            freopen("input.txt","r",stdin);
            freopen("output.txt","w",stdout);    
    #endif
      int test;
      cin>>test;
     for(int tst=1;tst<=test;tst++){
     	cout<<"Case #"<<tst<<": ";
     	for(int i=0;i<30;i++)
     		h[i]=0;
     	string s;
     	cin>>s;
     	for(int i=0;i<10;i++)
     		ans[i]=0;
     	int l=s.length();
     	for(int i=0;i<l;i++)
     		h[s[i]-'A']++;

     	int temp=0;
     	temp=h['Z'-'A'];
     	ans[0]=temp;
     	h['Z'-'A']-=temp;
     	h['E'-'A']-=temp;
     	h['R'-'A']-=temp;
     	h['O'-'A']-=temp;

     	temp=h['W'-'A'];
     	ans[2]=temp;
     	h['W'-'A']-=temp;
     	h['T'-'A']-=temp;
     	
     	h['O'-'A']-=temp;

     	temp=h['U'-'A'];
     	ans[4]=temp;
     	h['U'-'A']-=temp;
     	h['F'-'A']-=temp;
     	h['R'-'A']-=temp;
     	h['O'-'A']-=temp;

     	temp=h['X'-'A'];
     	ans[6]=temp;
     	h['X'-'A']=0;
     	h['I'-'A']-=temp;
     	h['S'-'A']-=temp;
     	

     	temp=h['G'-'A'];
     	ans[8]=temp;
     	h['G'-'A']=0;
     	h['E'-'A']-=temp;
     	h['I'-'A']-=temp;
     	h['T'-'A']-=temp;
     	h['H'-'A']-=temp;

     	temp=h['O'-'A'];
     	ans[1]=temp;
     	h['O'-'A']=0;
     	h['N'-'A']-=temp;
     	h['E'-'A']-=temp;

     	temp=h['H'-'A'];
     	ans[3]=temp;
     	h['H'-'A']=0;
     	h['T'-'A']-=temp;
     	h['R'-'A']-=temp;
     	h['E'-'A']-=temp;
     	h['E'-'A']-=temp;

     	temp=h['F'-'A'];
     	ans[5]=temp;
     	h['F'-'A']=0;
     	h['V'-'A']-=temp;
     	h['E'-'A']-=temp;
     	h['I'-'A']-=temp;

     	temp=h['I'-'A'];
     	ans[9]=temp;
     	h['I'-'A']=0;
     	h['N'-'A']-=temp;
     	h['E'-'A']-=temp;
     	h['N'-'A']-=temp;
     	

     	temp=h['S'-'A'];
     	ans[7]=temp;
     	h['E'-'A']=0;
     	h['S'-'A']-=temp;
     	h['V'-'A']-=temp;
     	h['E'-'A']-=temp;
     	h['N'-'A']-=temp;

     	for(int i=0;i<=9;i++)
     		for(int j=0;j<ans[i];j++)
     			cout<<i;
     		cout<<endl;
     	
     }
    return 0;  
}
