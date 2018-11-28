#include <iostream>
#include <set>

using namespace std;

bool isCompleted(int n, set<int> &nos)
{
    while (n > 0)
    {
        nos.insert(n % 10);
        n /= 10;
    }
    /* for (set<int>::iterator it=nos.begin(); it!=nos.end(); ++it) */
    /*     cout << ' ' << *it; */
    /* cout<<endl; */
    return nos.size() == 10;
}

int main(void)
{
    int t = 0;
    cin>>t;

    for (int i=0; i< t; i++)
    {
        int n = 0, n_step=0;
        cin>>n;
        
        if (n != 0)
        {
            set<int> nos;
            do {
                n_step += n;
            } while (!isCompleted(n_step, nos));
            cout << "Case #" << i+1 <<": "<< n_step << endl;
        }
        else 
        {
            cout << "Case #" << i+1 <<": INSOMNIA"<< endl;
        }
    }
}
