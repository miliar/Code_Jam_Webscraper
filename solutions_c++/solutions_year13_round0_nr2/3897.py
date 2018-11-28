#include <fstream>
using namespace std;
int main()
{
    int t,n,m,*mat,x,y;
    bool ver,hor;
    ifstream cin;
    ofstream cout;
    cin.open("input.txt");
    cout.open("output.txt");
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>n>>m;
        mat = new int [n*m];
        cout<<"Case #"<<i+1<<": ";
        for(int j=0;j<n*m;j++) cin>>mat[j];

        for(int j=0;j<n*m;j++)
        {
            ver=true; hor=true;
            x=j/m;
            y=j%m;
            //cout<<mat[x*m+y]<<endl;
            for(int k=0;k<m;k++) {if(mat[j]<mat[x*m+k]) {hor=false; break;}}
            for(int k=0;k<n;k++) {if(mat[j]<mat[k*m+y]) {ver=false; break;}}
            if(!(ver||hor)) goto L1;
        }
        cout<<"YES"<<endl; continue;
        L1:
        cout<<"NO"<<endl;
        delete [] mat;
    }
    cin.close();
    cout.close();
    return 0;
}
