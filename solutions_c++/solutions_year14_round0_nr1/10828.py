#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen ( "input.in","r",stdin);
freopen("output.out","w",stdout);
    int T,r,i,j,a[4],b[4],c[4],count=0,save,p=1;
    cin>>T;
    while(T--)
    {
        cin>>r;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if((i+1)==r)
                cin>>a[j];
                else
                cin>>c[j];
            }
        }
        cin>>r;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if((i+1)==r)
                cin>>b[j];
                else
                    cin>>c[j];
            }
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(b[j]==a[i]){
                    count+=1;
                    save=a[i];
                    break;}
            }
        }
        if(count==0)
        cout<<"Case #"<<p<<": Volunteer cheated!"<<endl;
        else if(count==1)
        cout<<"Case #"<<p<<": "<<save<<endl;
        else
        cout<<"Case #"<<p<<": Bad magician!"<<endl;
        p++;
        count=0;
    }
    fclose(stdin);
fclose(stdout);
    return 0;
}
