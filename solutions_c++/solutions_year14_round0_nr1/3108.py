#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t,i;
    /*ofstream myfile;
    myfile.open("cj1a.txt");
    ifstream myfile1;
    myfile1.open("A-small-attempt0.in.txt");
    myfile1>>t;*/
    cin>>t;
    for(i=0;i<t;i++)
    {
        int x,y,f1=0,d[4]={0},e[4]={0},b[4][4],c[4][4],j,k,a;
        cin>>x;
        for(j=0;j<4;j++)
        {
             for(k=0;k<4;k++)
             {
             cin>>b[j][k];
             if(j+1==x)
             d[k]=b[j][k];
             }
        }
        cin>>y;
        for(j=0;j<4;j++)
        {
             for(k=0;k<4;k++)
             {
             cin>>c[j][k];
             if(j+1==y)
             e[k]=c[j][k];
             }
        }
    //    for(j=0;j<4;j++)
      //      cout<<d[j]<<" "<<e[j]<<endl;
        for(j=0;j<4;j++)
        {
             for(k=0;k<4;k++)
             {
                   if(d[j]==e[k])
                   {
                   f1++;
        //           cout<<"hello"<<endl;
                   a=e[k];
                   }
             }
        }
        if(f1==1)
        cout<<"Case #"<<i+1<<": "<<a<<endl;
        else if(f1==0)
        cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
        else
        {
         //cout<<f1<<endl;
        cout<<"Case #"<<i+1<<": Bad magician!\n";
        }
    }
    //myfile.close();
  //  myfile1.close();
 return 0;
}
