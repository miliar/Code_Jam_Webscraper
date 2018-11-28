#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
using namespace std;
int fun(int arr[255],int p[255],int size,int arr_size){
    //size -> p size
    int shift = 0, i;
    for(i = 0; i < size; i++)
    {
        int temp = (arr[i] + p[i] + shift )%10;
        shift = (arr[i] + p[i] + shift) / 10;
        arr[i] = temp;
    }
    while(shift && i < 255)
    {
        int temp =( arr[i] +shift) % 10;
        shift = (arr[i] +shift) / 10;
        arr[i] = temp;
        i++;
    }
    if(arr_size < i)
        arr_size = i;
    return arr_size;//arr's digits
}
int main()
{
    int N, T;  bool bo = true;
    cin >> T;
    for(int time = 1; time <= T; time++)
    {
        cin >> N;
        if(N != 0){
            bo = true;
            int arr[255] = {0}, p[255] = {0}, arr_size, size, i, num[10] = {0};
        for(i = 0 ; N %10 || N/10; i++)
        {
            arr[i] = N % 10;  p[i] = N % 10; num[N % 10] = 1;
            N = N/10;   //cout << p[i];
           // cout << arr[i];
        }
        arr_size = i; size = i;
        for(int j = 0; bo;j++){
            bo = false;
            
            arr_size = fun(arr,p, size,arr_size);
           //cout << arr_size;
            for(i = arr_size - 1 ; i >= 0; i--)
             num[arr[i]] = 1; //cout << arr[i]<<",";}
           //cout << endl;
            for(i = 0; i < 10; i++) { if (num[i] == 0){ bo = true;}}
        }
        cout <<"Case #" << time <<": ";
        for(i = arr_size - 1; i >= 0; i--)
            cout << arr[i];
           // cout << "|" <<size;
        }
        else
            cout <<"Case #" << time <<": INSOMNIA";
        cout << endl;
            
    }
}