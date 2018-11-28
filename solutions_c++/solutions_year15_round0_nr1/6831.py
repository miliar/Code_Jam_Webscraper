#include <iostream>
#include <string>
using namespace std;

class audi
{
private:
        int sMax;
        string people;
public:
       void input();
       void output();
};

int main()
{
    int t;
    cin>>t;
    audi aud[1001];
    for(int i=0;i<t;i++)
    {
            aud[i].input();
    }
    
    for(int i=0;i<t;i++)
    {
            cout<<"Case #"<<i+1<<": ";
            aud[i].output();
            cout<<endl;
    }
    
    system("pause");
    return 0;
}

void audi::input()
{
     cin>>sMax;
     cin>>people;
}

void audi::output()
{
     int ans = 0, c = 0;
     
     c+=people[0]-48;
     
     for(int i=1;i<people.length();i++)
     {
             if(c<i && people[i]!='0')
             {
                    ans+=i-c;
                    c+=i-c;
             }
             c+=people[i]-48;
     }
     
     cout<<ans;
}
