    #include<bits/stdc++.h>
    #include <iostream>
    using namespace std;
    int main()
    {
    freopen("inp3.in","r",stdin);
    int t,limit,x,l,flag_i,flag_j,flag_k,i,j,k,number,negative;
    char inputString[10001];
    int arr[5][5]={{0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
    cin>>t;
    for(k = 1;k <= t;k++)
    {
    flag_i = flag_j = flag_k = negative = 0;
    cin>>l>>x;
    scanf("%s",inputString);
    limit= x * l;
    number = inputString[0] - 'i' + 2;
    if(number < 0)
    {
    number =- number;
    if(negative == 0)
    negative = 1;
    else
    negative = 0;
    }
     
    if(number == 2 && flag_i == 0 && negative == 0)
    {
    flag_i = 1;
    number = 1;
    }
     
    for(i = 1;i < limit;i++)
    {
    j = i % l;
    number = arr[number][inputString[j] - 'i' + 2];
    if(number < 0)
    {
    number = -number;
    if(negative == 0)
    negative = 1;
    else
    negative = 0;
    }
     
    if(number == 2 && flag_i == 0 && negative == 0)
    {
    flag_i = 1;
    number = 1;
    }
    else if(number == 3 && flag_i == 1 && flag_j == 0 && negative == 0)
    {
    flag_j = 1;
    number = 1;
    }
    else if(number == 4 && flag_i == 1 && flag_j == 1 && flag_k == 0 && negative == 0)
    {
    flag_k = 1;
    i++;
    number = 1;
    break;
    }
     
    }
    if(flag_k == 1)
    {
    number = 1;
    for(;i < limit;i++)
    {
    j = i % l;
    number = arr[number][inputString[j]-'i'+2];
    if(number < 0)
    {
    number = -number;
    if(negative == 0)
    negative = 1;
    else
    negative = 0;
    }
    }
    if(number == 1 && negative == 0)
    printf("Case #%d: YES\n",k);
    else
    printf("Case #%d: NO\n",k);
    }
    else
    printf("Case #%d: NO\n",k);
     
     
    }
    return 0;
    }