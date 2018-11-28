#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    int t,no,n1,i,j,test,a,coun;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>test;
    for(t=1;t<=test;t++){
        cin>>n1;
        coun=0;
        no=-1;
        vector<int> v;
        for(i=0;i<4;i++)
        {
          for(j=0;j<4;j++)
          {
              cin>>a;
              if((i+1)!=n1)
              {

              }
              else
              {
                  v.push_back(a);
              }
          }
        }
        sort(v.begin(),v.end());
        cin>>n1;
        for(i=0;i<4;i++)
        {
          for(j=0;j<4;j++)
          {
              cin>>a;
              if((i+1)!=n1)
              {

              }
              else
              {
                  if(binary_search(v.begin(),v.end(), a))
                     {
                         no=a;
                         coun++;
                     }
              }
          }
        }
        if(coun==1)
            cout<<"Case #"<<t<<": "<<no<<endl;
        else if(coun==0)
            cout<<"Case #"<<t<<": "<<"Volunteer cheated!"<<endl;
        else
            cout<<"Case #"<<t<<": "<<"Bad magician!"<<endl;


    }
}
