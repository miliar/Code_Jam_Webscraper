#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <map>
#include <string>


/* rand example: guess the number */
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */


using namespace std;

int main()
{/*
    int a [1000];
    int iSecret, iGuess;
    int i=0, j=0, k=0, temp=0 ;
    int max =1000;
    srand (time(NULL));
    int mean1=0 ,mean2=0;
    int c=0;
    
    
    */
    
    
    //int num, total = 0; 
    //int count=0;
    //int dec =0;
    //cout << "Please enter a decimal: ";
    //cin >> num;
    /*
    while(num > 0)
    {
        total = num % 2;
        num /= 2;
        dec = total*(10^count)
        cout << total;
        count++;
    }
    cout << endl;
    */
    
    //int a = 3, b =4;
    //int c= a & b;
    //cout << c << endl;
    //cout << 11 && 01 << endl;
    //cout << 10 && 11 << endl;
    int count =0;
    int i,j;
    int cn = 0;
    int case_num = 0;
    
    int a=0,b=0,k=0;
    int result=0;
    
    cin >> case_num;
    
    for ( cn = 0; cn < case_num; cn++) {
        
        count =0;
        result=0;
        
        cin >> a >> b >> k;
        
        
        
        for (i=0; i <a; i++) {
        
        for (j=0; j <b; j++) {
            result = i&j;
        //cout << result << endl;
        if (result < k) count++;
        
        }
        
        }
        
        
        
        
        cout << "Case #" << cn + 1 << ": ";
		
			cout << count << endl;
			
   }
    
    
    
//cout << count << endl;
    
    
    return 0;
    
    /*
    
    for ( k = 0; k < 120 ; k++) {
        
     for ( i = 0; i < max ; i++) {
         a[i]= i;
         }
         
     for ( i = 0; i < max ; i++) {
         
         j= rand() % max ; //test 1
        //j= rand() % (max-i) + i ; //test 2
         temp = a[i];
         a[i]=a[j];
         a[j]=temp;
         }
         */
     /*
     for ( i = 0; i < max; i++) {
         cout << a[i] << endl;
         //cout << endl;
         }
         */
     
     /*
     mean1 =0;
     for ( i = 0; i < max/2; i++){
         mean1=mean1+a[i];
         }
     mean1 = mean1 / (max / 2);
     cout << "first mean is " << mean1 << endl;
     
     mean2 =0;
     for ( i = max/2; i < max ; i++){
         mean2=mean2+a[i];
         }
     mean2 = mean2 / (max / 2);
     cout << "second mean is " << mean2 << endl;
     
     if (mean1<mean2 )
        c++;
         
     cout << endl;
     
     
     
}
    cout << "c is " << c <<  endl;
    */
}



