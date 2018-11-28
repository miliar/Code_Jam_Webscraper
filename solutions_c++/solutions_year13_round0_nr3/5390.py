#include <iostream>
#include <map>
#include <string>
#include <stdlib.h>
#include <cmath>
#include <cstdio>

using namespace std;
    map<int64_t,int> palinMap;
    map<int64_t,int>::iterator it;
    map<int64_t,int64_t> sqrtMap;
    //map<int64_t,int64_t>::iterator it;
//4 no
//5 yes
//bool isPalindrome(string n)
//    {
//        if(palinMap[n]==4)
//        {
//                return false;
//        }
//        if(palinMap[n]==5)
//        {
//                return true;
//        }
//
//        if (n == string(n.rbegin(), n.rend()))
//        {
//            //cout << n << " is a palindrome";
//            palinMap[n]=5;
//            return true;
//        }
//        palinMap[n]=4;
//        return false;
//    }

    bool isPalindrome(int64_t number)
    {
        if(palinMap[number]==4)
        {
                return false;
        }
        if(palinMap[number]==5)
        {
                return true;
        }

        int64_t palindrome = number;
        int64_t reverse = 0;

        while (palindrome != 0)
        {
            int64_t remainder = palindrome % 10;
            reverse = reverse * 10 + remainder;
            palindrome = palindrome / 10;
        }

        if (number == reverse)
        {
            palinMap[number]==5;
       //     palinMap[reverse]==5;
            return true;
        }
        palinMap[number]=4;
        //palinMap[reverse]=4;
        return false;
    }

    bool isSqrtPalindrome(int64_t sqNum)
    {
     //   cout<<"Sqrt Check for : "<<sqNum<<endl;
        if(sqNum==0)
        {
            return true;
        }
        long double sq;
        sq=sqNum*1.0;

        long double sqr=sqrt(sq);
        long double fractpart, intpart;


        fractpart = modf (sqr , &intpart);
       // cout<<"fract part : "<<fractpart<<endl;
        if(fractpart>0)
        {
            return false;
        }
        //cout<<"FractCheck passed : "<<sqNum<<" : int part : "<<intpart<<endl;
        //int64_t rdSqr=llround(intpart);
        //cout

        if(isPalindrome(intpart))
        {
           // cout<<"Intpart passes palindrome check : "<<intpart<<" : Orig : "<<sqNum<<endl;
            return true;
        }
        return false;
    }




int main()
{

    int T =0;
    int ct=0;
    string A;
    string B;
    int64_t nA;
    int64_t nB;
    int64_t j;
    int i;

    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w+",stdout);

    cin>>T;
    for(i=1;i<=T;i++)
    {
        ct=0;
        cin>>nA;
        cin>>nB;

        //nA=atoll(A);
        //nA=atoll(B);

            for(j=nA;j<=nB;j++)
            {
                if(isPalindrome(j))
                {
                    if(isSqrtPalindrome(j))
                    {
                        ct++;
                    }
                }
            }
            cout<<"Case #"<<i<<": "<<ct<<endl;
        }






    return 0;
}
