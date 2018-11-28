#include <iostream>
#include <map>
using namespace std;


int main()
{
    int T;
    int l = 1;
    cin >> T;

    while(T--)
    {
int newN;
        int N;
        int counter = 0;
        cin >> N;
        map<int, int> m;

if(N == 0)
    goto ans;


for(int i = 1; ;i++)
{

 newN = N*i;
int temp = newN;

while(temp > 0)
{
    int singleD = temp%10;
    temp = temp/10;
    if(m.find(singleD) == m.end())
    {

        m[singleD]++;
        counter++;

    }

    if(counter == 10)
    {
        goto ans;
    }
}


}
ans:
    if(counter == 0)
{
        cout << "Case #" << l << ": INSOMNIA" << endl;


}

else
cout << "Case #" << l << ": " << newN << endl;
l++;
    }




    return 0;
}
