#include<iostream>
#include<vector>
#include<queue>
#include<string>
#include<algorithm>
#include<sstream>

#define P 3.14

using namespace std;

void re(int y)
{
    static int x=0;
    x++;    
    cout<<"Case #"<<x<<": "<<y<<endl;
    
}

int main()
{
    //Number of Testcases
    int T;
    cin>>T;
    //Testcases

    /*
    //2-D matrix
    int m,n;
    cin>>m;
    cin>>n;
    //m=n;

    vector<vector<int> > mat;
    vector<int> row;
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
            row.push_back(0);
        mat.push_back(row);
    }
    //2-d Ends
    */
     
    int f,c;
    double r,t;
    double a,ar,d;
       
    for(int i=0;i<T;i++)
    {
        f=0;
        c=0;
        cin>>r>>t;
        a=r*r;
        while(1)
        {        
            ar=(r+1.0)*(r+1.0);   
            d=ar-a;
            if(t<d)
                f=1;
            else
            {
                t=t-d;
                c++;
            }
            if(f==1)
                break;
            a=(r+2.0)*(r+2.0);;
            r=r+2.0;
            //cout<<d<<t<<endl;
        }
        re(c);
    } 
    return 0;
}
