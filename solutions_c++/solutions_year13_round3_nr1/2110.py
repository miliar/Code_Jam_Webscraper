#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <utility>

using namespace std;

typedef pair<int,int> help;
help one;
set< help > final;

bool check(string temp,int n)
{

    for(int i=0;i<temp.size();i++)
    {
        if(temp[i]==97||temp[i]==101||temp[i]==105||temp[i]==111||temp[i]==117)return false;
    }
return true;
}

void sub (string name,int n)
{
    int size=name.size();

        for(int j=0;j+n<size+1;j++)
        {
            string temp=name.substr(j,n);
            if(check(temp,n))
            {
                for(int s=j;s>=0;s--)
                {
                    for(int e=j+n-1;e<size;e++)
                    {
                        one=make_pair(s,e);
                        final.insert(one);
                    }
                }

            }

        }
}

int main()
{
    fstream file;
    ofstream answer;
    file.open("A-small-attempt1.in");
    answer.open("answer.txt");

    int n=0,line=1;
    while(int temp=file.get())
    {
        if(temp==10)break;
        temp-=48;
        n=(n*10)+temp;
    }
    cout<<n<<endl;

    while (line!=n+1)
    {
        string name;
        int n;
        int ans;
        file>>name;
        file>>n;
        sub(name,n);
        ans=final.size();
        final.clear();
        cout<<"Case #"<<line<<": "<<ans<<endl;
        answer<<"Case #"<<line<<": "<<ans<<endl;
        line++;
    }
}
