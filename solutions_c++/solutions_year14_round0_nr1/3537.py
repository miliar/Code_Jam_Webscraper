#include <iostream>
#include<fstream>
using namespace std;
void input( int cards[4][4], int new_cards[4][4] , int &ans1 , int &ans2);
void output(int card[4][4]);
void initial(int card[4][4]);
int algo(int card[4][4], int card1[4][4],int row1 , int row2,int &count);
ifstream in("test1.txt",ios::in);
ofstream out("result.txt",ios::out);

int main()
{
     int i = 0,ans1 = 0 , ans2 = 0,check = 0 ,count = 0;
     char c;
    int test_cases = 0, cards[4][4], new_cards[4][4];
    in.get(c);
    cout<<c;
    while(c != '\n')
    {
        test_cases = (test_cases * 10) + (int)c - 48;
        in.get(c);
    }
    for(i = 0 ; i < test_cases ; i++)
    {
        check = 0;
        initial(cards);
        initial(new_cards);
        input(cards,new_cards,ans1,ans2);
        //cout<<"ans"<<ans1<<"ANS"<<ans2<<"\n";
        output(cards);
        output(new_cards);
        check = algo(cards,new_cards,ans1,ans2,count);
        if(check == 1)
        {
            cout<<"Case #"<<i+1<<": "<<count;
            out<<"Case #"<<i+1<<": "<<count<<"\n";
        }
        else if(check > 1)
        {
            cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<check;
            out<<"Case #"<<i+1<<": "<<"Bad magician!\n";
        }
        else if(check == 0)
        {
            cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<check;
            out<<"Case #"<<i+1<<": "<<"Volunteer cheated!\n";
        }
        cout<<"\n";
    }
    return 0;
}

void input( int cards[4][4], int new_cards[4][4], int  &ans1 , int &ans2)
{
     int i = 0 , r = 0 ,t = 0;
     ans1 = 0,ans2 = 0;
     char c;
        in.get(c);
        while(c != '\n')
        {

            ans1 = (ans1 * 10) + (int)(c - 48);
            in.get(c);
        }


        for(t = 0 ; t < 4 ; t++)
        {
            for(r = 0 ; r < 4 ; r++)
            {
               in.get(c);
               while(c != ' ' && c != '\n')
               {
                   cards[t][r] = (cards[t][r] * 10) + (int)c - 48;
                   in.get(c);
               }
            }
        }

        in.get(c);
        while(c != '\n')
        {
            ans2 = (ans2 * 10) + (int)(c - 48);
            in.get(c);
        }
        //ans2 = &ans;
        for(t = 0 ; t < 4 ; t++)
        {
            for(r = 0 ; r < 4 ; r++)
            {
               in.get(c);
               while(c != ' ' && c != '\n' && !in.eof() )
               {
                   new_cards[t][r] = (new_cards[t][r] * 10 ) + (int)c - 48;
                   in.get(c);
               }
            }
        }
        while(c != '\n' && !in.eof())
        {
            in.get(c);
        }


}

void output(int card[4][4])
{
    int i = 0 , j = 0;
    for(i = 0 ; i < 4 ; i++)
    {
        for(j = 0 ; j < 4; j++)
        {
            cout<<card[i][j]<<" ";
        }
        cout<<"\n";
    }
}

void initial(int card[4][4])
{
    int i = 0 , j = 0;
    for(i = 0 ; i < 4 ; i++)
    {
        for(j = 0 ; j < 4 ; j++)
        {
            card[i][j] = 0;
        }
    }
}

int algo(int card[4][4], int card1[4][4] , int n , int m ,int &common)
{
    int i = 0 , j = 0,count = 0;
    char c;
    for(i = 0 ; i < 4 ; i++)
    {
        for(j = 0 ; j < 4; j++)
        {
            if(card[n-1][i] == card1[m-1][j])
            {
                count++;
                if(count == 1)
                {
                    common = card[n-1][i];
                }
                    //cout<<"COUNT"<<count;
                //cin>>c;
            }
        }
    }
    if(count > 1)
    {
        common = -1;
    }
    //cout<<"count"<<count;
    return count;

}
