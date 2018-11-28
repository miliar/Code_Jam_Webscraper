    #include <iostream>

    using namespace std;

    int recurseCountDigits(int number, int digit){
        if(number < 10) {

            return number == digit ? 1 : 0;
        } else {

            if(number%10 == digit) {

                return 1 ;
            } else {

                return recurseCountDigits(number/10, digit);
            }
        }
    }

    int main()
    {
        int t;
        cin>>t;
        for(int k=1;k<=t;k++)
        {
            int n,c[10]={0},j=1,flag=0,curr;
            cin>>n;
            if(n==0)
            {
                cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
                continue;
            }
            curr=n;
            while(1)
            {
                for(int i=0;i<10;i++)
                {
                    if(c[i]==0)
                    {
                          c[i]=c[i]+recurseCountDigits(curr,i);
                          if(c[i]!=0)flag += i+1;
                    }


                }
                if(flag>=55)
                {
                    cout<<"Case #"<<k<<": "<<curr<<endl;
                    break;
                }
                else
                {
                    j++;
                    curr=n*j;
                }
            }


        }

        return 0;
    }
