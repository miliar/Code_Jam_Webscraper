#include<iostream>
using namespace std;

class v
{

    int ma[4][4];
    int first[4];
    int second[4];
    public:
     int ans;
    int row_no;
    v()
    {
        ans=-1;
    }
    void givearrange()
    {
        int i,j;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>ma[i][j];
            }
        }
    }
    void f()
    {
     int i;
     for(i=0;i<4;i++)
     first[i]=ma[row_no-1][i];
    }
   void s()
    {
      int i;
     for(i=0;i<4;i++)
     second[i]=ma[row_no-1][i];
    }
    int compare()
    {
        int i,j,c=0;

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {if(first[i]==second[j])
            c++;}
        }
        if(c==1)
         {
           for(i=0;i<4;i++)
           {
               for(j=0;j<4;j++){
               if(first[i]==second[j])
               ans=first[i];}
           }
           return 1;
         }
         else if(c>1)
         {
             return 2;
         }
         else if(c==0)
         {
             return 3;
         }
    }
};
int main()
{
    int n,n1,i=0;
    cin>>n;
    n1=n;
    v object[n];
    while(n!=0)
    {
        cin>>object[i].row_no;
        object[i].givearrange();
        object[i].f();
        cin>>object[i].row_no;
        object[i].givearrange();
        object[i].s();
        n--;
        i++;
    }
    i=0;
   while(n1!=0)
   {
       int temp;
    temp=object[i].compare();
    switch(temp)
    {
        case 1:cout<<"Case #"<<i+1<<": "<<object[i].ans<<"\n";
               break;
        case 2:cout<<"Case #"<<i+1<<": Bad magician!"<<"\n";
               break;
        case 3:cout<<"Case #"<<i+1<<": Volunteer cheated!"<<"\n";
               break;
    }
    n1--;
    i++;
   }
   return 0;
}
