#include <iostream>
#include <vector>

using namespace std;

int digits_no(int N)
{
    int count=0;
    while(N!=0)
    {
     if(N/10==0)
     {
        return count+1;
     }
     else
     {
        N=N/10;
        count++;
     }
    }
}

void dig_change(bool *check, int N, int dig_no)
{
    for(int i=0; i< dig_no; i++)
    {
        check[N%10]=true;
        N= N/10;
    }
}

bool allpresent(bool *check)
{
    for(int l=0; l<10; l++)
    {
        if(check[l]==true)
        {
            continue;
        }
        else
        {
            return false;
            break;
        }
    }
    return true;
}


int main()
{
    int no_of_case;
    cin >> no_of_case;
    int N;
    int i=0;
    bool check[10];
    for(int k=0; k<no_of_case; k++)
    {
     cin >> N;
     int M=N;
     if(N==0)
     {
        cout<< "Case #"<< i+1<< ":"<< " " << "INSOMNIA"<< '\n';
        i++;
     }
     else
     {
        for(int l=0; l<10; l++)
        {
            check[l]= false;
        }
        int count=1;
        while(true)
        {
            int dig_no;
            dig_no = digits_no(N);
            dig_change(check, N, dig_no);
            //cout << "The N is:"<< N << '\n';
            if(!allpresent(check))
            {
                N=(count+1)*M;
                count++;
            }
            else
            {
                cout<< "Case #"<< i+1 << ":"<< " " << N << '\n';
                i++;
                break;
            }
        }
     }
    }
}
