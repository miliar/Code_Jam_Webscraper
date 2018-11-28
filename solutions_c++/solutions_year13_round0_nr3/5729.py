#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
ofstream fout("result.out");
void next_p(const vector<int> & original, vector<int> & result)
{
            bool toExceed = true;
            int l_o_index = 0;
            int r_o_index = original.size()-1;
            int l_r_index = 0;
            int r_r_index = result.size()-1;
            while(l_o_index!= r_o_index && l_o_index != r_o_index-1)
            {
                              if(original[l_o_index]<9)
                              {
                               toExceed = false;    
                              }                              
                              l_o_index++;
                              r_o_index--;
                              l_r_index++;
                              r_r_index--;                          
            }
            if(original[l_o_index]<9)
            {
                               toExceed = false;    
            }
            if(toExceed)
            {
             result[0]=1;
             result.push_back(1);
             for(int i = 1; i < result.size()-1;i++)
                    result[i]=0;
            }
            else
            {
                if(result[l_r_index]<9&& l_r_index==r_r_index-1)
                {
                                         result[l_r_index]+=1;result[r_r_index]+=1;
                }
                if(result[l_r_index]<9&&l_r_index==r_r_index)
                {
                                                             result[l_r_index]+=1;
                }
                else if(result[l_r_index]==9)
                {
                    while(result[l_r_index]==9&&l_r_index!=0&&r_r_index!=result.size()-1)
                    {
                                               l_r_index--;
                                               r_r_index++;
                    }
                    result[l_r_index]+=1;
                    result[r_r_index]+=1;
                }
            }
            
}

void bigSquare(const vector<int> & original, vector<int> & result)
{
     int i, j, k;  
    int tmp;  
  
    for (i = 0; i < original.size(); ++i)   
    {  
        k = i;  
        for (j = 0; j < original.size(); ++j)  
        {  
            result[k++] += original[i] * original[j];  
        }  
    }  
      
    for (k = result.size() - 1;  k >= 0; --k)   
    {  
        if (result[k] > 9)   
        {  
            if (k != 0)  
            {  
                  
                result[k-1] += result[k] / 10;  
                result[k] %= 10;  
            }  
            else
            {     
                tmp = result[k] / 10;  
                result[k] %=10;  
                result.insert(result.begin(), tmp);  
            }  
        }  
    }
}
bool isP(const vector<int> & num)
{
     int l_index = 0;
     int r_index = num.size()-1;
     while(l_index!= r_index && l_index != r_index-1)
     {
                     if(num[l_index]!=num[r_index])
                     return false;
                     else
                     l_index++;
                     r_index--;
     }
     if(num[l_index]!=num[r_index]) return false;
     return true;
}

bool is_Between(const vector<int> & start ,const vector<int> & end ,const vector<int> & data)
{
     if(data.size()>end.size()||data.size()<start.size())return false;
     if(data.size()<end.size()&&data.size()>start.size())return true;
     if(start.size()<end.size())
     {
                                if(data.size()==start.size())
                                {
                                  int i = 0;
                                  while(data[i] == start[i]&&i!=data.size()-1)
                                  {i++;}                                  
                                  if(data[i] < start[i]) return false;                                  
                                  return true;
                                }
                                if(data.size()==end.size())
                                {
                                  int i = 0;
                                  while(data[i] == end[i]&&i!=data.size()-1)
                                  {i++;}
                                  if(data[i] > end[i]) return false;
                                  return true;
                                }
     }
     if(start.size()==end.size())
     {
              int i = 0;
              while(data[i] == start[i]&&i!=data.size()-1)
              {i++;}                                  
              if(data[i] < start[i]) return false;
              i = 0;
              while(data[i] == end[i]&&i!=data.size()-1)
              {i++;}
              if(data[i] > end[i]) return false;
              return true;
     }
}

bool is_Bigger(const vector<int> & end ,const vector<int> & data)
{
     if(data.size()>end.size())return true;
     if(data.size()<end.size())return false;     
     if(data.size()==end.size())
     {
              int i = 0;
              while(data[i] == end[i]&&i!=data.size()-1)
              {i++;}
              if(data[i] > end[i]) return true;
              return false;
     }
}

void print(const vector<int> & num)
{
    for(int i = 0 ;i < num.size();++i){fout << num[i];}
    fout << "  ";
}
int main()
{
    ifstream fin("C-small-attempt2.in");
    if(!fin)
    {
        cout << "Error in reading!" << endl;
        return -1;
    }    
    int i=0,totalnum=0;
    fin >> totalnum;
    while(i<totalnum)
    {
         int count = 0;
         string start,end;                     
         vector<int> start_num,end_num;
         fin >> start >> end;
         for(int index = 0;index < start.size();++index)
                 start_num.push_back(start[index] - '0');                     
         for(int index = 0;index < end.size();++index)
                 end_num.push_back(end[index] - '0');
         int start_size = (start_num.size()+1)/2;
         //fout << "start_size" << start_size << endl;
         vector<int> square_num(start_size*2-1,0);
         vector<int> current_num(start_size,0);
         current_num[0] = 1;
         current_num[start_size-1] = 1; 
         vector<int> next_num(current_num);
         //fout <<" current before---" <<endl;
         //print(current_num);
         bigSquare(current_num,square_num);         
         while(!is_Between(start_num,end_num,square_num)&&!is_Bigger(end_num,square_num))
         {             
             next_p(current_num,next_num);
             //fout <<" next before---" <<endl;
             //print(next_num);
             current_num.clear();
             current_num.assign(next_num.begin(),next_num.end());
             square_num.clear();
             square_num.assign(current_num.size()*2-1,0);             
             bigSquare(current_num,square_num);
             //fout <<" start---" <<endl;             
             //print(start_num);
             //fout <<" end---" <<endl;                          
             //print(end_num);
             //fout <<"square before---" <<endl;                                       
             //print(square_num);                          
         }
             //fout <<"---------current_____________" <<endl;
             //print(current_num);         
         //print(start_num);
         while(is_Between(start_num,end_num,square_num))
         {
             if(isP(square_num))
             {
                 //print(square_num);
                 count++;
             }
             //fout <<" next---" <<endl;                                       
             //print(next_num);             
             next_p(current_num,next_num);
             current_num.clear();
             current_num.assign(next_num.begin(),next_num.end());
             square_num.clear();
             square_num.assign(current_num.size()*2-1,0);
             bigSquare(current_num,square_num);                         
             //fout << "start---"<<endl;
             //print(start_num);
             //fout << "end---"<<endl;             
             //print(end_num);
             //fout <<" square---" <<endl;             
             //print(square_num);               
         }
         //print(end_num);         
         //fout << endl;
         fout <<"Case #"<<(i+1)<<": "<< count << endl;
         //fout << "-------------------------------------"<<endl;
         i++;
    }
    system("PAUSE");
    return 0;
}
