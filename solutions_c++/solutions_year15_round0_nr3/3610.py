#include <iostream>
#include <string>
#include <fstream>




using namespace std;
char matrix[10001][10001];

int main()
{
    ifstream fin;   // 定义一个文件输入流
    ofstream fout; //cout<< --> fileout<<
    fin.open("data.in");
    fout.open("data.out");
    long T,X,L;
    long i,j,k,flag1,flag2;
    char input_str[10000];
    char input[10000];
    int result[100];

    fin>>T;
    for (i=0;i<=T-1;++i)
    {
        fin>>L>>X;
        fin>>input_str;
        result[i]=1;
        flag1=0;
        if (L*X<=2) {result[i]=0;continue;}
        for (j=0;j<=L-1;++j) {if (input_str[j]!=input_str[0]) {flag1=1;break;}}
        if (flag1==0) {result[i]=0;continue;}
        result[i]=0;
        //input=input_str*X;
        for (j=0;j<=X-1;++j)
        {
            for (k=0;k<=L-1;++k) input[j*L+k]=input_str[k];
        }
        //cout<<L*X<<endl;
        for (j=0;j<=L*X-1;++j)
        {
            matrix[j][j+1]=input[j];
            matrix[j+1][j]='+';
        }
        for (j=2;j<=L*X;++j)
        {
            for (k=0;k<=L*X-j;++k)
            {
                if ((matrix[j+k-1][k]=='+' && matrix[j+k][j+k-1]=='+') || (matrix[j+k-1][k]=='-' && matrix[j+k][j+k-1]=='-'))
                {
                if (matrix[k][j+k-1]=='1'&&matrix[j+k-1][j+k]=='1') {matrix[k][j+k]='1';matrix[j+k][k]='+';}
                if (matrix[k][j+k-1]=='1'&&matrix[j+k-1][j+k]=='i') {matrix[k][j+k]='i';matrix[j+k][k]='+';}
                if (matrix[k][j+k-1]=='1'&&matrix[j+k-1][j+k]=='j') {matrix[k][j+k]='j';matrix[j+k][k]='+';}
                if (matrix[k][j+k-1]=='1'&&matrix[j+k-1][j+k]=='k') {matrix[k][j+k]='k';matrix[j+k][k]='+';}

                if (matrix[k][j+k-1]=='i'&&matrix[j+k-1][j+k]=='1') {matrix[k][j+k]='i';matrix[j+k][k]='+';}
                if (matrix[k][j+k-1]=='i'&&matrix[j+k-1][j+k]=='i') {matrix[k][j+k]='1';matrix[j+k][k]='-';}
                if (matrix[k][j+k-1]=='i'&&matrix[j+k-1][j+k]=='j') {matrix[k][j+k]='k';matrix[j+k][k]='+';}
                if (matrix[k][j+k-1]=='i'&&matrix[j+k-1][j+k]=='k') {matrix[k][j+k]='j';matrix[j+k][k]='-';}

                if (matrix[k][j+k-1]=='j'&&matrix[j+k-1][j+k]=='1') {matrix[k][j+k]='j';matrix[j+k][k]='+';}
                if (matrix[k][j+k-1]=='j'&&matrix[j+k-1][j+k]=='i') {matrix[k][j+k]='k';matrix[j+k][k]='-';}
                if (matrix[k][j+k-1]=='j'&&matrix[j+k-1][j+k]=='j') {matrix[k][j+k]='1';matrix[j+k][k]='-';}
                if (matrix[k][j+k-1]=='j'&&matrix[j+k-1][j+k]=='k') {matrix[k][j+k]='i';matrix[j+k][k]='+';}

                if (matrix[k][j+k-1]=='k'&&matrix[j+k-1][j+k]=='1') {matrix[k][j+k]='k';matrix[j+k][k]='+';}
                if (matrix[k][j+k-1]=='k'&&matrix[j+k-1][j+k]=='i') {matrix[k][j+k]='j';matrix[j+k][k]='+';}
                if (matrix[k][j+k-1]=='k'&&matrix[j+k-1][j+k]=='j') {matrix[k][j+k]='i';matrix[j+k][k]='-';}
                if (matrix[k][j+k-1]=='k'&&matrix[j+k-1][j+k]=='k') {matrix[k][j+k]='1';matrix[j+k][k]='-';}
                }

                if ((matrix[j+k-1][k]=='-' && matrix[j+k][j+k-1]=='+') || (matrix[j+k-1][k]=='+' && matrix[j+k][j+k-1]=='-'))
                {
                if (matrix[k][j+k-1]=='1'&&matrix[j+k-1][j+k]=='1') {matrix[k][j+k]='1';matrix[j+k][k]='-';}
                if (matrix[k][j+k-1]=='1'&&matrix[j+k-1][j+k]=='i') {matrix[k][j+k]='i';matrix[j+k][k]='-';}
                if (matrix[k][j+k-1]=='1'&&matrix[j+k-1][j+k]=='j') {matrix[k][j+k]='j';matrix[j+k][k]='-';}
                if (matrix[k][j+k-1]=='1'&&matrix[j+k-1][j+k]=='k') {matrix[k][j+k]='k';matrix[j+k][k]='-';}

                if (matrix[k][j+k-1]=='i'&&matrix[j+k-1][j+k]=='1') {matrix[k][j+k]='i';matrix[j+k][k]='-';}
                if (matrix[k][j+k-1]=='i'&&matrix[j+k-1][j+k]=='i') {matrix[k][j+k]='1';matrix[j+k][k]='+';}
                if (matrix[k][j+k-1]=='i'&&matrix[j+k-1][j+k]=='j') {matrix[k][j+k]='k';matrix[j+k][k]='-';}
                if (matrix[k][j+k-1]=='i'&&matrix[j+k-1][j+k]=='k') {matrix[k][j+k]='j';matrix[j+k][k]='+';}

                if (matrix[k][j+k-1]=='j'&&matrix[j+k-1][j+k]=='1') {matrix[k][j+k]='j';matrix[j+k][k]='-';}
                if (matrix[k][j+k-1]=='j'&&matrix[j+k-1][j+k]=='i') {matrix[k][j+k]='k';matrix[j+k][k]='+';}
                if (matrix[k][j+k-1]=='j'&&matrix[j+k-1][j+k]=='j') {matrix[k][j+k]='1';matrix[j+k][k]='+';}
                if (matrix[k][j+k-1]=='j'&&matrix[j+k-1][j+k]=='k') {matrix[k][j+k]='i';matrix[j+k][k]='-';}

                if (matrix[k][j+k-1]=='k'&&matrix[j+k-1][j+k]=='1') {matrix[k][j+k]='k';matrix[j+k][k]='-';}
                if (matrix[k][j+k-1]=='k'&&matrix[j+k-1][j+k]=='i') {matrix[k][j+k]='j';matrix[j+k][k]='-';}
                if (matrix[k][j+k-1]=='k'&&matrix[j+k-1][j+k]=='j') {matrix[k][j+k]='i';matrix[j+k][k]='+';}
                if (matrix[k][j+k-1]=='k'&&matrix[j+k-1][j+k]=='k') {matrix[k][j+k]='1';matrix[j+k][k]='+';}
                }


            //cout<<j<<' '<<k<<endl;
            }
        }
        //for (j=0;j<=11;++j) {for (k=0;k<=12;++k) cout<<matrix[j][k]<<' '; cout<<endl;}

        flag2=0;
        for (j=1;j<=L*X;++j)
        {
            if (matrix[0][j]=='i' &&matrix[j][0]=='+')
            {
                for (k=0;k<=L*X-1;++k)
                {
                    if (matrix[k][L*X]=='k' && matrix[L*X][k]=='+')
                    {
                        if (matrix[j][k]=='j' && matrix[k][j]=='+') {result[i]=1;flag2=1;break;}
                    }
                }
                if (flag2==1) break;
            }
        }
    cout<<"f";
    }
    for (i=0;i<=T-1;++i)
    {
        if (result[i]==1)
            fout<<"Case #"<<i+1<<": "<<"YES";
        else
            fout<<"Case #"<<i+1<<": "<<"NO";
        if (i!=(T-1)) fout<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
