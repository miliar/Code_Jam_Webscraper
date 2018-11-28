#include<iostream>
using namespace std;
int lawn[100][100];
//Capital M and N denotes dimension of land, small ones are variable
bool colp(int N,int m,int number)
{
    //cout<<"checkcolumn"<<m<<endl;
    int h=number;
    //cout<<"h="<<h<<endl;
    for(int n=0;n<N;n++)
    {
        //cout<<"current number:"<<n<<m<<" "<<lawn[n][m]<<endl;
        if(lawn[n][m]>h)return 0;
    }
    return 1;
}
bool rowp(int n,int M,int number)
{
    //cout<<"checkrow"<<n<<endl;
    int h=number;
    //cout<<"h="<<h<<endl;
    for(int m=0;m<M;m++)
    {
        //cout<<"current number:"<<n<<m<<" "<<lawn[n][m]<<endl;
        if(lawn[n][m]>h)return 0;
    }
    return 1;
}
bool possible(int N,int M)
{
    int nn;
    //iterate through the numbers
    for(int n=0;n<N;n++)
    {
        for(int m=0;m<M;m++)
        {
            nn=lawn[n][m];
            //cout<<"checking number"<<n<<m<<" "<<lawn[n][m]<<endl;
            if(!rowp(n,M,nn)&&!colp(N,m,nn))return 0;
        }
    }
    return 1;
}
int main(){
    int T;
    cin>>T;
    int N,M;
    string s;
    for(int t=1;t<=T;t++)
    {
        cin>>N>>M;
        for(int n=0;n<N;n++)
        {
            for(int m=0;m<M;m++)
            {
                cin>>lawn[n][m];
            }
        }
        if(possible(N,M))s="YES";
        else s="NO";
        cout<<"Case #"<<t<<": "<<s<<endl;
    }
}
