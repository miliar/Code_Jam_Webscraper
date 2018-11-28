#include<cstdio>
#include<string>
#include<iostream>
#include<deque>
using namespace std;
string str;
deque<char>temp;
deque<char>answer;
void update()
{
    for(int i=0;i<str.size();i++)
    {
        if(answer[i]>temp[i])
	    return;
	if(answer[i]<temp[i])
	    break;
    }
    for(int i=0;i<str.size();i++)
	answer[i]=temp[i];
    return;
}
void backtracking(int index)
{
    if(index==str.size())
    {
        update();
    }
    else
    {
        temp.push_back(str[index]);
	backtracking(index+1);
        temp.pop_back();

	temp.push_front(str[index]);
	backtracking(index+1);
	temp.pop_front();
    }
}
int main(void)
{
    int cases;
    scanf("%d",&cases);
    getline(cin,str);
    for(int i=1;i<=cases;i++)
    {
	answer.clear();
	temp.clear();
	getline(cin,str);
        //for(int j=0;i<str.size();j++)
	    //answer.push_back(0);
        answer.resize(str.size());
        temp.push_back(str[0]);
	backtracking(1);
        printf("Case #%d: ",i);
        for(int j=0;j<str.size();j++)
	    printf("%c",answer[j]);
        printf("\n");	
    }
    return 0;

}
