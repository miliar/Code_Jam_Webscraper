#include <iostream>

using namespace std;
signed char buffer[120];

int searchChange(int n)
{
    for(int i=0;i<n;i++)
        if(buffer[i]!=buffer[i+1])
            return i;
    return n;
}

int order(int n)
{
    int change = searchChange(n);
    if (change == n) return n;
    int limit = change/2;
    for(int i=0;i<=limit;i++)
    {
        char aux = buffer[i];
        buffer[i] = -buffer[change-i];
        buffer[change-i] = -aux;
    }
    return change;
}

void processCase(int position, string &sequence)
{
    int n = (int)sequence.length();
    int counter = 0;
    int lastPosition;
    for(int i=0; i<n;i++)
    {
        buffer[i] = sequence[i]=='+'?1:-1;
    }
    buffer[n] = 1;

    while(true)
    {
        lastPosition = order(n);
        if (lastPosition==n)
             break;
        counter++;
    }

    cout<<"Case #"<<position<<": "<<counter<<endl;
}

int main()
{
    int n;
    int c;
    string sequence;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>sequence;
        processCase(i+1, sequence);
    }

}
