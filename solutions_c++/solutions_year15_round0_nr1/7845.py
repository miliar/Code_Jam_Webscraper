#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("g.txt","w",stdout);
    string str;
    int cs,i,ar[10004],csno,ekhn;
    scanf("%d",&csno);
for(ekhn=1; ekhn<=csno; ekhn++)
{


    scanf("%d",&cs);
    //scanf("%s",str.c_str());
    cin>>str;
    //cout<<str<<" lo\n";
    for
        (i=0; i<=cs; i++)
    {
        ar[i]=str[i]-'0';
        //cout<<ar[i]<<"\t";
        //scanf("%d",&ar[i]);
    }
    //cout<<"baire \n";
    int lagbe=-1;
    for (i=cs; i>=0; i--)
    {
        if (ar[i]>=0)
        {
            lagbe= max(i, (lagbe-ar[i]) );
        }
    }
    printf("Case #%d: ",ekhn);
    if (lagbe>=1)
        cout<<lagbe<<endl;
    else cout<<"0\n";

}


while(1);
    return 0;
}
