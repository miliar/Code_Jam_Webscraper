#include <iostream>
#include <cstdio>
#include <stack>
#include <sstream>

using namespace std;

int main() {
    freopen("C:/Users/Esam/Desktop/input.txt","r",stdin);
    freopen("C:/Users/Esam/Desktop/output.txt","w",stdout);

    int T;
    cin>>T;

    for(int t=0;t<T;t++)
    {
        cout<<"Case #"<<t+1<<": ";

        string in;
        cin>>in;

        int size=0;
        int it=0;
        stringstream ssin(in);


        char* arr;
        arr = new char[size];

        while (ssin.good() && it < in.size()){
            ssin >> arr[it];
            ++it;
            size++;
        }

        int start=0,end=size-1;
        int flipped=0;
        int noOfPositive=0;

        while(start<=end)
        {
            if(arr[start]=='-')
                break;
            if(arr[start]=='+')
            {
                noOfPositive++;
            }
            start++;
        }

        start=0;

        while(start!=end+1)
        {
            if(arr[start]=='-' && arr[end]=='-')
            {
                for(int lo=0;lo<end+1;lo++)
                {
                    switch (arr[lo]) {
                    case '+':
                        arr[lo]='-';
                        break;
                    case '-':
                        arr[lo]='+';
                        break;
                    }
                }
                int temp;
                while(start<end)
                {
                    temp=arr[start];
                    arr[start]=arr[end];
                    arr[end]=temp;
                    end--;
                    start++;
                }
                noOfPositive=0;
                end=size-1;
                start=0;
                while(start<=end)
                {
                    if(arr[start]=='-')
                        break;
                    if(arr[start]=='+')
                    {
                        noOfPositive++;
                    }
                    start++;
                }
                end=size-1;
                start=0;
                flipped++;
            }
            else
            {
                if(arr[start]=='+')
                {
                    if(noOfPositive==size)  break;
                    for(int lo=0;lo<noOfPositive;lo++)
                    {
                        arr[lo]='-';
                    }

                    noOfPositive=0;
                    end=size-1;
                    start=0;
                    while(start<=end)
                    {
                        if(arr[start]=='-')
                            break;
                        if(arr[start]=='+')
                        {
                            noOfPositive++;
                        }
                        start++;
                    }

                    end=size-1;
                    start=0;
                    flipped++;
                }
                else
                {
                    end--;
                }
            }
        }
        cout<<flipped<<endl;
    }
}


