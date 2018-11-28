#include<bits/stdc++.h>
using namespace std;

int main()
{

    freopen("A-large.txt", "w", stdout);
    freopen("A-large.in", "r", stdin);
    int TC;
    string input;
    int arr[200];
    cin>>TC;
    string number[] = {"ZERO", "TWO", "SIX",  "SEVEN",  "FOUR", "FIVE", "ONE",  "NINE", "EIGHT","THREE" };
    int idx[]       = { 0, 2, 6, 7, 4, 5, 1, 9, 8, 3};
    int num[10];

    for(int t=1; t<=TC; t++)
    {
        memset(arr, 0, sizeof arr);
        memset(num, 0, sizeof num);
        cin>>input;

        for(int i=0; i<input.length(); i++)
        {
            arr[input[i]]++;
        }
        cout<<"Case #"<<t<<": ";


        for(int i=0; i<10; i++)
        {
            while(true)
            {
                bool isF = false;
                for(int j=0; j<number[i].length(); j++)
                {
                    if(arr[number[i][j]]<=0) isF = true;
                    arr[number[i][j]]--;

                }
                if(isF)
                {
                    for(int j=0; j<number[i].length(); j++)
                    {
                        arr[number[i][j]]++;;
                    }
                    break;
                }
                else
                    num[idx[i]]++;

            }
        }
        for(int i=0; i<10; i++)
        {
            while(num[i]!=0)
                {
                    cout<<i;
                    num[i]--;
                }
        }
        cout<<endl;

    }
}
