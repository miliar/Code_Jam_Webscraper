# include<iostream>
using namespace std;
int save[10];
int prev[10];
void init()
{
    int i;
    for(i=0;i<10;i++)
    {
        save[i]=0;
        prev[i]=0;
    }
}
long long int compute(long long int n)
{
    long long int t = n;
    //cout  << n << endl;
    while(n>0)
    {
        save[n%10]++;
        n=n/10;
    }
    /*for(int x=0;x<10;x++)
        cout << save[x] << " " ;
    cout << endl; */
    int flag=0;
    int i;
    for(i=0;i<10;i++)
    {
        if(save[i]!=prev[i])
        {
            flag=1;
            break;
        }
    }
    if(flag==0)
        return -1;
    else
    {

        for(i=0;i<10;i++)
            prev[i]=save[i];
        flag=0;
        for(i=0;i<10;i++)
        {
            if(save[i]==0)
                return 0;
        }
       // cout << t << endl;
        return t;
    }
}
int main()
{
    int test;
    cin >> test;
    int temp = test;
    long long int n,i;
    long long int num;
    long long int t;
    while(test>0)
    {
        init();
        cin >> n;
        i=1;
       // int p=1;
        while(true)
        {
           // p++;
            num = n * i;
            i++;
            t = compute(num);
            if(t==-1)
            {
                cout << "Case #" << (temp-test+1) << ": INSOMNIA" << endl;
                break;
            }
            else if(t!=0)
            {
                //cout  << "helo"<< endl;
                cout << "Case #" << (temp-test+1) << ": " << compute(t) << endl;
                break;
            }
        }
        test--;
    }
}
