#include<iostream>
#include<algorithm>
#include<cstdio>

using namespace std;

int inp(int a[4][4])
{
    for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
            cin>>a[i][j];
}

void check(int n1, int a1[4][4], int n2, int a2[4][4], int t)
{
    int tmp1[4], tmp2[4];
    for(int i=0; i<4; i++)
    {
        tmp1[i] = a1[n1-1][i];
        tmp2[i] = a2[n2-1][i];
    }

    int counter = 0;
    int num;
    for(int i=0; i<4; i++)
    {
        if(find(tmp1, tmp1+4, tmp2[i]) != tmp1+4)
        {
            counter++;
            num = tmp2[i];
        }

    }

    if(counter == 0)
    {
        cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
    }

    else if(counter == 1)
    {
        cout<<"Case #"<<t<<": "<<num<<endl;
    }

    else if(counter > 1)
        cout<<"Case #"<<t<<": Bad magician!"<<endl;

}


int main(void)
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("result1.in", "w", stdout);
    int t;
    cin>>t;
    string res[t];
    for(int i=0; i<t; i++)
    {
        int n1, n2;
        cin>>n1;
        int a1[4][4], a2[4][4];
        inp(a1);
        cin>>n2;
        inp(a2);
        check(n1, a1, n2, a2, i+1);
    }
    return 0;
}
