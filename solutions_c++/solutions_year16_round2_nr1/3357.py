#include<bits/stdc++.h>
using namespace std;

int num1[10][27];

int main()
{

    freopen("0in.txt","r",stdin);
    freopen("0out.txt","w",stdout);
    num1[0]['Z'-'A']=1;num1[0]['E'-'A']=1;num1[0]['R'-'A']=1;num1[0]['O'-'A']=1;
    num1[1]['O'-'A']=1;num1[1]['N'-'A']=1;num1[1]['E'-'A']=1;
    num1[2]['T'-'A']=1;num1[2]['W'-'A']=1;num1[2]['O'-'A']=1;
    num1[3]['T'-'A']=1;num1[3]['H'-'A']=1;num1[3]['R'-'A']=1;num1[3]['E'-'A']=2;
    num1[4]['F'-'A']=1;num1[4]['O'-'A']=1;num1[4]['U'-'A']=1;num1[4]['R'-'A']=1;
    num1[5]['F'-'A']=1;num1[5]['I'-'A']=1;num1[5]['V'-'A']=1;num1[5]['E'-'A']=1;
    num1[6]['S'-'A']=1;num1[6]['I'-'A']=1;num1[6]['X'-'A']=1;
    num1[7]['S'-'A']=1;num1[7]['E'-'A']=2;num1[7]['V'-'A']=1;num1[7]['N'-'A']=1;
    num1[8]['E'-'A']=1;num1[8]['I'-'A']=1;num1[8]['G'-'A']=1;num1[8]['H'-'A']=1;num1[8]['T'-'A']=1;
    num1[9]['N'-'A']=1;num1[9]['I'-'A']=1;num1[9]['E'-'A']=1;

    int ts,i,j,l,p;
    scanf("%d",&ts);

    for(int kk1=1;kk1<=ts;kk1++)
    {

    string ss;
    int ar[10]={0},chr[27]={0};
    cin>>ss;
    l=ss.size();

    for(i=0;i<l;i++)
        chr[ss[i]-'A']++;

    p=chr['Z'-'A'];
    ar[0]=p;

    for(i=0;i<27;i++)
        chr[i]-=p*num1[0][i];
    p=chr['W'-'A'];
    ar[2]=p;

    for(i=0;i<27;i++)
        chr[i]-=p*num1[2][i];
     p=chr['X'-'A'];
    ar[6]=p;



    for(i=0;i<27;i++)
        chr[i]-=p*num1[6][i];

    p=chr['G'-'A'];
    ar[8]=p;

    for(i=0;i<27;i++)
        chr[i]-=p*num1[8][i];
    p=chr['U'-'A'];
    ar[4]=p;

    for(i=0;i<27;i++)
        chr[i]-=p*num1[4][i];
     p=chr['O'-'A'];
    ar[1]=p;

    for(i=0;i<27;i++)
        chr[i]-=p*num1[1][i];
    p=chr['T'-'A'];
    ar[3]=p;

    for(i=0;i<27;i++)
        chr[i]-=p*num1[3][i];
    p=chr['F'-'A'];
    ar[5]=p;

    for(i=0;i<27;i++)
        chr[i]-=p*num1[5][i];
    p=chr['V'-'A'];
    ar[7]=p;

    for(i=0;i<27;i++)
        chr[i]-=p*num1[7][i];
    p=chr['I'-'A'];
    ar[9]=p;

    for(i=0;i<27;i++)
        chr[i]-=p*num1[9][i];

    printf("Case #%d: ",kk1);


    for(i=0;i<=9;i++)
        for(j=0;j<ar[i];j++)
    printf("%d",i);


    printf("\n");

    }


}
