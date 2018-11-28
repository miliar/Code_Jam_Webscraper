#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    fstream f,f2;
    f.open("A-large.in",ios::in);
    f2.open("A-large.out",ios::out);
    f>>t;
    for(int j=1;j<=t;j++)
    {
        int arr[26]={0};
        int ctr;
        string word;
        f>>word;
        ctr=word.length();
        for(int i=0;i<word.length();i++)
        {
            char c=word[i];
            arr[(c-(int)'A')]++;
        }
        int freq[10]={0};
        int temp;

        if(arr[('Z'-(int)'A')]>0)
        {
            temp=arr[('Z'-(int)'A')];
            arr[('Z'-(int)'A')]=0;
            arr[('E'-(int)'A')]-=temp;
            arr[('R'-(int)'A')]-=temp;
            arr[('O'-(int)'A')]-=temp;
            freq[0]=temp;
        }

        if(arr[('W'-(int)'A')]>0)
        {
            temp=arr[('W'-(int)'A')];
            arr[('W'-(int)'A')]=0;
            arr[('T'-(int)'A')]-=temp;
            arr[('O'-(int)'A')]-=temp;
            freq[2]=temp;
        }

        if(arr[('X'-(int)'A')]>0)
        {
            temp=arr[('X'-(int)'A')];
            arr[('X'-(int)'A')]=0;
            arr[('S'-(int)'A')]-=temp;
            arr[('I'-(int)'A')]-=temp;
            freq[6]=temp;
        }

        if(arr[('G'-(int)'A')]>0)
        {
            temp=arr[('G'-(int)'A')];
            arr[('G'-(int)'A')]=0;
            arr[('E'-(int)'A')]-=temp;
            arr[('I'-(int)'A')]-=temp;
            arr[('H'-(int)'A')]-=temp;
            arr[('T'-(int)'A')]-=temp;
            freq[8]=temp;
        }

        if(arr[('H'-(int)'A')]>0)
        {
            temp=arr[('H'-(int)'A')];
            arr[('H'-(int)'A')]=0;
            arr[('T'-(int)'A')]-=temp;
            arr[('R'-(int)'A')]-=temp;
            arr[('E'-(int)'A')]-=temp;
            arr[('E'-(int)'A')]-=temp;
            freq[3]=temp;
        }

        if(arr[('S'-(int)'A')]>0)
        {
            temp=arr[('S'-(int)'A')];
            arr[('S'-(int)'A')]=0;
            arr[('E'-(int)'A')]-=temp;
            arr[('V'-(int)'A')]-=temp;
            arr[('E'-(int)'A')]-=temp;
            arr[('N'-(int)'A')]-=temp;
            freq[7]=temp;
        }

        if(arr[('V'-(int)'A')]>0)
        {
            temp=arr[('V'-(int)'A')];
            arr[('V'-(int)'A')]=0;
            arr[('E'-(int)'A')]-=temp;
            arr[('I'-(int)'A')]-=temp;
            arr[('F'-(int)'A')]-=temp;
            freq[5]=temp;
        }

        if(arr[('F'-(int)'A')]>0)
        {
            temp=arr[('F'-(int)'A')];
            arr[('F'-(int)'A')]=0;
            arr[('O'-(int)'A')]-=temp;
            arr[('U'-(int)'A')]-=temp;
            arr[('R'-(int)'A')]-=temp;
            freq[4]=temp;
        }

        if(arr[('O'-(int)'A')]>0)
        {
            temp=arr[('O'-(int)'A')];
            arr[('O'-(int)'A')]=0;
            arr[('E'-(int)'A')]-=temp;
            arr[('N'-(int)'A')]-=temp;
            freq[1]=temp;
        }

        if(arr[('N'-(int)'A')]>0)
        {
            temp=arr[('N'-(int)'A')];
            arr[('N'-(int)'A')]=0;
            arr[('I'-(int)'A')]-=temp;
            arr[('N'-(int)'A')]-=temp;
            arr[('E'-(int)'A')]-=temp;
            freq[9]=temp/2;
        }

        f2<<"Case #"<<j<<": ";
        for(int i=0;i<=9;i++)
        {
            for(int k=0;k<freq[i];k++)
                f2<<i;
        }
        f2<<endl;
    }
    f.close();
    f2.close();
}
