#include <iostream>
#include <iomanip>
#include <string>
#include <cstring>
#include <cstdio>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <list>
#include <map>
#include <fstream>
using namespace std;
#define MAX_N 101
string flip(string s,int pos)
{
    string next=s;
    for(int i=0;i<=pos;i++)
    {
        if(s[pos-i]=='+')next[i]='-';
        else next[i]='+';
    }
    return next;
}
bool last(string s)
{
    for(int i=0;i<s.length();i++)
        if(s[i]=='-')return false;
    return true;
}
int bfs(string s)
{
    queue<string> q;
    map<string,bool>visited;
    map<string,int>dis;
    string current=s;
    q.push(s);
    visited[s]=true;
    dis[s]=0;
    if(last(s))return 0;
    while(!q.empty())
    {
        current=q.front();
        q.pop();
        int d=dis[current];
        for(int i=0;i<current.length();i++)
        {
            string next=flip(current,i);
            if(visited.find(next)==visited.end()){q.push(next);dis[next]=d+1;visited[next]=true;}
            if(last(next))return d+1;
        }
    }
}
int minFlips(string s)
{
    if(last(s))return 0;
    for(int i=s.length()-1;i>=0;i--)
    {
        if(s[i]=='-')
        {
            if(s[0]=='-')return 1+minFlips(flip(s,i));
            else return 2+minFlips(flip(flip(s,0),i));
        }
    }
}
int main()
{
    ifstream fin;
    fin.open("B-small-attempt2.in");
    ofstream fout;
    fout.open("B.txt");
    int T;
    fin>>T;
    for(int t=1;t<=T;t++)
    {
        string s;
        fin>>s;
        fout<<"Case #"<<t<<": "<<bfs(s)<<endl;
    }
}
