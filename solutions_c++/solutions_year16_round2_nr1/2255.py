#include<bits/stdc++.h>
using namespace std;

int num[10][27];

int main()
{
    num[0]['Z'-'A']=1;num[0]['E'-'A']=1;num[0]['R'-'A']=1;num[0]['O'-'A']=1;
    num[1]['O'-'A']=1;num[1]['N'-'A']=1;num[1]['E'-'A']=1;
    num[2]['T'-'A']=1;num[2]['W'-'A']=1;num[2]['O'-'A']=1;
    num[3]['T'-'A']=1;num[3]['H'-'A']=1;num[3]['R'-'A']=1;num[3]['E'-'A']=2;
    num[4]['F'-'A']=1;num[4]['O'-'A']=1;num[4]['U'-'A']=1;num[4]['R'-'A']=1;
    num[5]['F'-'A']=1;num[5]['I'-'A']=1;num[5]['V'-'A']=1;num[5]['E'-'A']=1;
    num[6]['S'-'A']=1;num[6]['I'-'A']=1;num[6]['X'-'A']=1;
    num[7]['S'-'A']=1;num[7]['E'-'A']=2;num[7]['V'-'A']=1;num[7]['N'-'A']=1;
    num[8]['E'-'A']=1;num[8]['I'-'A']=1;num[8]['G'-'A']=1;num[8]['H'-'A']=1;num[8]['T'-'A']=1;
    num[9]['N'-'A']=1;num[9]['I'-'A']=1;num[9]['E'-'A']=1;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,ts,i,j,l,p;
    scanf("%d",&ts);

    for(t=1;t<=ts;t++)
    {

    string s;
    int ar[10]={0},chr[27]={0};
    cin>>s;
    l=s.size();

    for(i=0;i<l;i++)
        chr[s[i]-'A']++;

    p=chr['Z'-'A'];
    ar[0]=p;
    //cout<<p<<endl;
    for(i=0;i<27;i++)
        chr[i]-=p*num[0][i];
    p=chr['W'-'A'];
    ar[2]=p;
    //cout<<p<<endl;
    for(i=0;i<27;i++)
        chr[i]-=p*num[2][i];
     p=chr['X'-'A'];
    ar[6]=p;
    //cout<<p<<endl;
    for(i=0;i<27;i++)
        chr[i]-=p*num[6][i];

    p=chr['G'-'A'];
    ar[8]=p;
    //cout<<p<<endl;
    for(i=0;i<27;i++)
        chr[i]-=p*num[8][i];
    p=chr['U'-'A'];
    ar[4]=p;
   // cout<<p<<endl;
    for(i=0;i<27;i++)
        chr[i]-=p*num[4][i];
     p=chr['O'-'A'];
    ar[1]=p;
    //cout<<p<<endl;
    for(i=0;i<27;i++)
        chr[i]-=p*num[1][i];
    p=chr['T'-'A'];
    ar[3]=p;
    //cout<<p<<endl;
    for(i=0;i<27;i++)
        chr[i]-=p*num[3][i];
    p=chr['F'-'A'];
    ar[5]=p;
   // cout<<p<<endl;
    for(i=0;i<27;i++)
        chr[i]-=p*num[5][i];
    p=chr['V'-'A'];
    ar[7]=p;
   // cout<<p<<endl;
    for(i=0;i<27;i++)
        chr[i]-=p*num[7][i];
    p=chr['I'-'A'];
    ar[9]=p;
    //cout<<p<<endl;
    for(i=0;i<27;i++)
        chr[i]-=p*num[9][i];
    printf("Case #%d: ",t);
    for(i=0;i<=9;i++)
        for(j=0;j<ar[i];j++)
    printf("%d",i);
    printf("\n");

    }


}
