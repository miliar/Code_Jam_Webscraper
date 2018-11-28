#include<fstream>
#include<vector>
#include<string>

using namespace std;

int func(string s,int a)
{
    int chk = 0;
    for(int i=0;i<s.size();i++)
    {
        if(s[i]=='a' || s[i]=='e'|| s[i]=='i' || s[i]=='o' || s[i]=='u')
            chk = 0;
        else
        {
            chk++;
            if(chk == a)
                return 1;
        }
    }
    return 0;
}

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt",ios::out);
    int T;
    in>>T;
    for(int a=0;a<T;a++)
    {
        string s;
        in>>s;
        int n;
        in>>n;
        int rt = 0;
        for(int i=n;i<=s.size();i++)
        {
            for(int j=0;(j+i)<=s.size();j++)
            {
                string temp;
                for(int k=0;k<i;k++)
                    temp.push_back(s[j+k]);
                if(func(temp,n))
                    rt++;
            }
        }
        out<<"Case #"<<a+1<<": "<<rt<<endl;
    }
    return 0;
}
