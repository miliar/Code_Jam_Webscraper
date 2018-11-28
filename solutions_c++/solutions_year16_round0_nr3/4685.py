#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t,j,k,n,l,m,z;
    char fin[100],fout[100];
    cin>>fin>>fout;
    ofstream outfile;
    ifstream infile;
    outfile.open (fout);
    infile.open(fin);
    infile>>t;
    infile>>n>>j;
    //t=1;
    //n=16;
    //j=50;
    int p=0;
    long long int num=pow(2,n-1)-1,temp;
    outfile<<"Case #1:"<<endl;
    while(p<j)
    {
        string tp="";
        num=num+2;
        //cout<<num<<endl;
        temp=num;
        while(temp)
        {
            if(temp%2==0)
                tp="0"+tp;
            else
                tp="1"+tp;
            temp=temp/2;
        }
        //cout<<num<<endl;
        long long int lst[12]= {0};
        for(l=0; l<n; l++)
        {
            for(m=2; m<=10; m++)
            {
                lst[m]=pow(m,l)*(tp[n-1-l]-'0')+lst[m];
            }
        }
        //cout<<tp<<endl;
        //outfile<<"Case #"<<p<<": "<<tp;
        //for(m=2;m<=10;m++)
          //  cout<<lst[m]<<endl;
        long long int res[12]= {0},y;
        for(y=2; y<=10; y++)
        {
            int check=0;
            /*if(lst[y]%2==0)
            {
                res[y]=2;
                continue;
            }*/
            for(z=2; z<=sqrt(lst[y]); z=z+1)
            {
                //cout<<z<<"  JJJ"<<endl;
                if(lst[y]%z==0)
                {
                    res[y]=z;
                    //cout<<z<<"  JJJ"<<endl;
                    check=1;
                    break;
                }
            }
            if(check==0)
                break;
        }
        if(y==11)
        {
            outfile<<tp;
            for(int y=2; y<=10; y++)
                outfile<<" "<<res[y];
            outfile<<endl;
            p++;
        }
    }
    outfile.close();
    infile.close();
    return 0;
}

