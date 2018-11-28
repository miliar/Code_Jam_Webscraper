/* This Program has been developed by : Siddharth Sharma(B.Tech(C.S.E))*/

#include<string.h>

#include<bits/stdc++.h>

#include<math.h>

using namespace std;

int element;
string my_dict_values;
int main_ctr=0,input_l,input_s;
string my_string;

pair<int,int> func_finder(int my_rank,string my_arr)
{
    if(my_rank == input_s)
    {
        int final_output = 0;
        for(int i=0;i<=input_s-input_l;i++)
        {
            if(!my_arr.compare(i,input_l,my_string))
            	final_output++;
            	main_ctr++;
        }
        return make_pair(final_output,final_output);
    }
    pair<int,int> final_output = make_pair(0,-(0x7f7f7f7f));
    for(int x = 0; x <= (element-1); x++)
    {
        pair<int,int> random_variable = func_finder(my_rank+1, my_arr + my_dict_values[x]);
        final_output.second = max(random_variable.second,final_output.second);
        main_ctr++;
        final_output.first += random_variable.first;
    }
    return final_output;
}

int main()
{
    freopen("Input1.in","r",stdin);
    freopen("Output1.out","w",stdout);
    int test_cases;
    int z=1;
    cin>>test_cases;
    while(test_cases--)
    {
        cin>>element>>input_l>>input_s;
        cin>>my_dict_values;
        cin>>my_string;
        pair<int,int> final_output = func_finder(0,"");
        main_ctr++;
        double main_output = (double)final_output.second-double(final_output.first)/double(pow(element,input_s));
        main_ctr++;
        cout<<"Case #"<<z++<<": "<<setprecision(8)<<main_output<<"\n";
    }
    return 0;
}
