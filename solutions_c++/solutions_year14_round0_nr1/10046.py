#include<iostream>

using namespace std;
int main()
{
   // cout<<"blah";
    int arr[4][4],i,j,test,*ar,k,l,an,fi;
    cin>>test;
    for(i=0;i<test;i++)
    {

        for(j=0;j<2;j++)
        {
            cin>>an;
            an=an-1;
            for(k=0;k<4;k++)
            {
                for(l=0;l<4;l++)
                {
                    cin>>arr[k][l];

                }

            }
            if(j==0)
            {
                ar=new int[4]  ;
                for(k=0;k<4;k++)
                {
                    ar[k]=arr[an][k];
                }
            }
            if(j==1)
            {
                l=0;
                for(k=0;k<4;k++)
                {
                 for(int x=0;x<4;x++)
                 {
                    if(ar[x]==arr[an][k])
                    {
                        l++;
                        fi=arr[an][k];
                    }
                 }
                }
                if(l==0)
                    cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
                else if(l==1)
                    cout<<"Case #"<<i+1<<": "<<fi<<endl;
                else if(l>1)
                {
                    cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
                }
            }
        }

    }
return 0;
}