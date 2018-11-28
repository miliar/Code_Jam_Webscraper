#include <bits/stdc++.h>
using namespace std;

int array[10]={1,0,0,0,0,0,0,0,0,0};
int check(void){
        for(int i=0; i<=9; i++)
        {
                if(i!=array[i])
                        return 0;
        }
        return 1;
}

void resetarray(void) {
    array[0]=1;
    for(int i=1;i<=9;i++)
        array[i]=0;
}

int main(int argc, char const *argv[]) {
        long int testCase,n,product,i,bit,number,result,status;
        long int flag=0,loopCount=0,caseNo=1,count=1,bitFlag=0;

        cin>>testCase;
        while(testCase!=0) //Loops with every testCase and prints the result
        {       flag=0;
                cin>>n;
                while (true) //Calculates the product and checks if all digits are present
                {       bitFlag=0;
                        number=product=n*count;
                        if(number/10==0)
                        {
                            array[number]=number;
                            bitFlag=1;
                        }
                        while (true) //Adds the bits into array
                        {
                                if (bitFlag==1) {
                                    break;
                                }
                                bit=number%10;
                                array[bit]=bit;
                                number=number/10;
                                if(number==0)
                                        break;
                        }
                        status=check();

                        if(status)
                        {
                                result=(n*(count+1))-n;
                                break;
                        }
                        loopCount++;
                        ++count;
                        if(loopCount>1000000000)
                        {
                                flag=1;
                                break;
                        }
                }

                if(flag)
                        cout<<"Case #"<<caseNo<<": INSOMNIA"<<endl;
                else
                        cout<<"Case #"<<caseNo<<": "<<result<<endl;

                --testCase;
                ++caseNo;
                resetarray();
                flag=0;loopCount=0;count=1;bitFlag=0;
        }
        return 0;
}
