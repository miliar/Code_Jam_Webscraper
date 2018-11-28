#include<iostream>

using namespace std;

int main()
{
    unsigned long long int A, motes[100], temp, count;
    int N, T;
    cin>>T;
    for (int i=0;i<T;i++)
    {
        cin>>A>>N;
        for (int j=0;j<N;j++)
            cin>>motes[j];
        for (int j=0;j<N;j++)
        {
            int small, pos;
            small = motes[j];
            pos=j;
            for (int k=j+1;k<N;k++)
            {
                if (motes[k]<small)
                {
                    small = motes[k];
                    pos = k;
                }
            }
            temp = motes[j];
            motes[j] = small;
            motes[pos] = temp;
        }
        count=0;
        for (int j=0;j<N;j++)
        {
            if (motes[j]<A)
                A = A+motes[j];
            else 
            {
                int iteration = 0;
                while (A <= motes[j])
                {
                    A = 2*A-1;
                    iteration++;
                    if (iteration>=(N-j))
                        break;
                }
                if (iteration >= N-j)
                {
                    count = count + N-j;
                    break;
                }
                else
                {
                    A= A+motes[j];
                    count = count + iteration;
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<count<<"\n";
    }
    return 0;
}
