#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;
main()
{
    int t,n,i,j,count,add;
    cin>>t;
    ofstream myfile;
    myfile.open ("standing ovation.txt");
    for(j=0;j<t;j++)
    {
        count=0;
        add=0;
        cin>>n;
        char s[n+1];
        cin>>s;
        for(i=0;i<strlen(s);i++)
        {
            if(count>=i)
                count=count+s[i]-48;
            else
            {
                add += i-count;
                count=i+s[i]-48;
            }
        }


        myfile << "case #"<<j+1<<":"<<" "<<add<<endl;;

//        cout<<"case #"<<j+1<<":"<<" "<<add<<endl;
    }
    myfile.close();
}
