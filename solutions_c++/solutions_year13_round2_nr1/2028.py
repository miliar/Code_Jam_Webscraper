#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int counter=0;
bool done=false;
int size,balls;
vector<int> ball;

int check(int beg,int &small)
{
    for(int i=beg;i<balls;i++)
        {
             if(small>ball[i])
                small+=ball[i];

             else
                return i;

        }

        return balls;
}

int func (int size,int beg)
{
    int step=0,temp;
    beg=check(beg,size);
    if(beg<balls)
    {
        step++;
        size+=size-1;
        temp=func(size,beg);

        if(temp<balls-beg)
        {
            step+=temp;
        }
        else
        {
            step=balls-beg;
        }

        return step;
    }

    else
    {
        return 0;
    }
}

int main()
{
    fstream file;
    ofstream answer;
    file.open("A-large (1).in");
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
        file>>size;
        file>>balls;
        ball.resize(balls);

        for(int i=0;i<balls;i++)
        {
            file>>ball[i];
        }

        sort(ball.begin(),ball.end());
        if(size==1)
        {counter= (balls);}
        else
        counter=func(size,0);

        cout<<"Case #"<<line<<": "<<counter<<endl;
        answer<<"Case #"<<line<<": "<<counter<<endl;
        line++;

    }
}
