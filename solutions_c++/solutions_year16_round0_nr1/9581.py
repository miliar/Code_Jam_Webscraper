//
//  main.cpp
//  test4
//
//  Created by Khaled on 4/9/16.
//  Copyright © 2016 Khaled. All rights reserved.
//

#include <iostream>
#include <string>
#include <sstream>
using namespace std;
template <typename T>
string NumberToString ( T Number )
{
    ostringstream ss;
    ss << Number;
    return ss.str();
}
int main(int argc, const char * argv[]) {
    // insert code here...
    int n;
    cin>>n;
    int theNumber;
    int counter = 1;
    while(counter<=n)
    {
        int arr[10];
        memset(arr, 0, sizeof(arr));
        cin>> theNumber;
        cout<<"Case #"<<counter<<": ";
        if (theNumber == 0)
        {
            cout<<"INSOMNIA";
        }
        else
        {
            int i = 1;
            int breakCounter = 0;
            while(breakCounter < 10)
            {
//                if arr[]
                
                string str = NumberToString(i*theNumber);
                for(int index = 0; index< str.length(); index++)
                {
                    if ( arr[str[index] - '0'] == 0)
                        breakCounter++;
                    arr[str[index] - '0'] = 1;
                }
                i++;
            }
            cout<<(i-1)*theNumber;
            
                
        }
        cout<<endl;
        counter++;
        
    }
    return 0;
}
