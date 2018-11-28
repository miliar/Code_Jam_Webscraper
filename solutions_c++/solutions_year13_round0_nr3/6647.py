#include<iostream>
#include<cmath>
using namespace std;
bool is_pallindrome(int number)
{
    int x=number;
    int rem=0;
    int rev=0;
    while(x>0)
    {
        rem=x%10;
        rev=(rev*10)+rem;
        x/=10;
    }
    if(rev==number)
        return true;
    else
        return false;
}
bool test(int number)
{
    float root=sqrt(number);
    int base=floor(root);
    if(base!=root)
        return false;
    if(is_pallindrome(base)&&is_pallindrome(number))
        return true;
}
int main()
{
    int t;
    int case_id;
    case_id=1;
    cin>>t;
    int a,b;
    int counter=0;
    while(case_id<=t)
    {
        cin>>a>>b;
        counter=0;
        for(int i=a;i<=b;i++)
        {
            if(test(i))
            {
                counter++;
            }
        }
        cout<<"Case #"<<case_id<<": "<<counter<<"\n";
        case_id++;
    }
}










