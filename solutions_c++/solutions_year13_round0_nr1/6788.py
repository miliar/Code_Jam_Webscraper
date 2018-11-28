# include<iostream>
# include<fstream>
# include<vector>
# include<string>
# include<stdio.h>
# include<stdlib.h>
# include<stddef.h>

using namespace std;
int isxwon(vector <string> row,vector <string> col,vector <string> dia)
{
    int i,j;
    for(i=0;i<4;i++)
    {
        if(row[i].compare("XXXX")==0||row[i].compare("XXXT")==0||row[i].compare("XXTX")==0||row[i].compare("XTXX")==0||row[i].compare("TXXX")==0)
            return 1;
    }
    for(i=0;i<4;i++)
    {
        if(col[i].compare("XXXX")==0||col[i].compare("XXXT")==0||col[i].compare("XXTX")==0||col[i].compare("XTXX")==0||col[i].compare("TXXX")==0)
            return 1;
    }
    for(i=0;i<2;i++)
    {
        if(dia[i].compare("XXXX")==0||dia[i].compare("XXXT")==0||dia[i].compare("XXTX")==0||dia[i].compare("XTXX")==0||dia[i].compare("TXXX")==0)
            return 1;
    }
    return 0;
}
int isowon(vector <string> row,vector <string> col,vector <string> dia)
{
    int i,j;
    for(i=0;i<4;i++)
    {
        if(row[i].compare("OOOO")==0||row[i].compare("OOOT")==0||row[i].compare("OOTO")==0||row[i].compare("OTOO")==0||row[i].compare("TOOO")==0)
            return 1;
    }
    for(i=0;i<4;i++)
    {
        if(col[i].compare("OOOO")==0||col[i].compare("OOOT")==0||col[i].compare("OOTO")==0||col[i].compare("OTOO")==0||col[i].compare("TOOO")==0)
            return 1;
    }
    for(i=0;i<2;i++)
    {
        if(dia[i].compare("OOOO")==0||dia[i].compare("OOOT")==0||dia[i].compare("OOTO")==0||dia[i].compare("OTOO")==0||dia[i].compare("TOOO")==0)
            return 1;
    }
    return 0;
}
int main()
{
    int t,i,j,ind=1,dot=0;
    unsigned found;
    cin>>t;
    ofstream op;
    op.open("output.txt");
    while(t--)
    {
        string s;
        vector <string> row;
        vector <string> col;
        vector <string> diagonal;
        for(i=0;i<4;i++)
        {
            cin>>s;
            found=s.find('.');
            if(found!=std::string::npos)
                dot=1;
            row.push_back(s);
        }
    //    cout<<"column\n";
        for(i=0;i<4;i++)
        {
            string temp="";
            for(j=0;j<4;j++)
            {
                temp+=row[j][i];
            }
      //      cout<<temp<<endl;
            col.push_back(temp);
        }
      //  cout<<endl<<endl;
        string temp="";
        temp+=row[0][3];
        temp+=row[1][2];
        temp+=row[2][1];
        temp+=row[3][0];
        diagonal.push_back(temp);
     //   cout<<temp<<endl;
        temp="";
        temp+=row[0][0];
        temp+=row[1][1];
        temp+=row[2][2];
        temp+=row[3][3];
        diagonal.push_back(temp);
   //     cout<<temp<<endl;
        if(isxwon(row,col,diagonal))
        {
            op<<"Case #"<<ind<<": "<<"X won\n";
        }
        else if(isowon(row,col,diagonal))
        {
            op<<"Case #"<<ind<<": "<<"O won\n";
        }
        else if(dot)
        {
            op<<"Case #"<<ind<<": "<<"Game has not completed\n";
        }
        else
        {
            op<<"Case #"<<ind<<": "<<"Draw\n";
        }
        ind++;
        dot=0;
    }

}
