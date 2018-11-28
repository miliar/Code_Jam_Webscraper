#include <iostream>
#include <string>
#include <vector>

using namespace std;
bool check(char c, vector <string> list)
{
    int d1 = 0;
    int d2 = 0;
    bool flag = false;
    for(int i = 0; i < 4; i++)
    {
        int l = 0;
        //cout<<list[i]<<"\n";
        for(int j = 0; j < 4; j++)
        {
            if(list[i][j] == c || list[i][j] == 'T')
                l++;
            if(i==j)
                {
                    if(list[i][j]==c||list[i][j]=='T')
                    d1++;
                }
            if(i+j==3)
                {
                    if(list[i][j]==c||list[i][j]=='T')
                    d2++;
                }
            
        }
        //cout<<"d1-"<<d1<<" d2-"<<d2<<" l-"<<l;
        if(l==4)
        flag = true;
    }
    if(d1==4||d2==4)
    flag = true;
    //cout<<flag;
    for(int i = 0; i < 4; i++)
    {
        int l2 = 0;
        //cout<<list[i]<<"\n";
        for(int j = 0; j < 4; j++)
        {
            if(list[j][i]==c||list[j][i]=='T')
            l2++;
        }
        if (l2==4)
        flag = true;
    }
    return flag;
}
int main() {
    int test,waste;
    cin>>test;
    for(int z = 1; z<=test; z++)
    {
        cout<<"Case #"<<z<<": ";
        vector <string> list;
        bool draw = true;
        for(int i = 0 ; i< 4; i++)
        {
            string s;
            cin>>s;
            list.push_back(s);
            for(int j = 0; j<4; j++)
            if(s[j]=='.')
            draw = false;
        }
        //int temp = (check('O', list));
        //cout<<temp;
        if(!check('O', list)&&!check('X',list)&&draw)
        cout<<"Draw"<<"\n";
        else if(check('X',list))
        cout<<"X won"<<"\n";
        else if(check('O',list))
        cout<<"O won"<<"\n";
        else 
        cout<<"Game has not completed"<<"\n";
        
    }
	return 0;
}