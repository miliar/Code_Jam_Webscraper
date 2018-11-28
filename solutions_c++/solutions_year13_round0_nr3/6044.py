#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <cstdio>
#include <sstream>

using namespace std;

vector<int> increment(vector<int> a);
vector<int> decrement(vector<int> a);
bool isZero(vector<int> a);
vector<int> vec_square(vector<int> a);
int vec_compare(vector<int> a, vector<int> b);
bool is_fair(vector<int> a);
void vec_read(vector<int> a);

int main()
{
    //variables
    ifstream file;
    file.open("C-small-attempt0.in");
    string line;
    getline(file, line);
    int T = atoi(line.c_str());
    cout<<"T: "<<T<<endl;
    ofstream file_out;
    file_out.open("C-small-attempt0.out");
    int result = 0;
    bool loop;

    vector<int> low_limit;
    vector<int> high_limit;
    
    
    //get the data case by case
    for(int n = 1; n <= T; n++)
    {
        getline(file, line);
        istringstream f(line);
        string hight, width, s;
        getline(f, hight, ' ');
        

        for(int i = hight.length() - 1; i >= 0;i--)
        {
            s = hight[i];
            low_limit.push_back(atoi(s.c_str()));
        }
        cout<<"low limit: ";
        vec_read(low_limit);

        getline(f, width, ' ');
        
        for(int i = width.length() - 1; i >= 0;i--)
        {
            s = width[i];
            high_limit.push_back(atoi(s.c_str()));
        }
        cout<<"High limit";
        vec_read(high_limit);


        vector<int> x(1);
        x[0] = 1;

        //increment x until its square reach to the lower limit
        while(vec_compare(vec_square(x), low_limit) == 2)
        {
            x = increment(x);
        }

        cout<<"=====low=========\n";
        cout<<"x: ";
        vec_read(x);
        cout<<"x square: ";
        vec_read(vec_square(x));
        cout<<"===============\n";

        //check if x is fair
        while(vec_compare(vec_square(x), high_limit) == 2 || vec_compare(vec_square(x), high_limit) == 0)
        {
            if(is_fair(x))
            {
                if(is_fair(vec_square(x)))
                    result++;
            }
            x = increment(x);
            cout<<"-----within---->";
            vec_read(x);
        }

        cout<<"======high=======\n";
        cout<<"x: ";
        vec_read(x);
        cout<<"x square: ";
        vec_read(vec_square(x));
        cout<<"=================\n";


        cout<<"Case #"<<n<<": "<<result<<endl;
        file_out<<"Case #"<<n<<": "<<result<<endl;
        result = 0;
        low_limit.clear();
        high_limit.clear();
        x.clear();
    }
    
    file.close();
    file_out.close();
	
	return 0;
}

vector<int> increment(vector<int> a)
{
    for(int i = 0; i <= a.size();i++)
    {
        if(i == a.size())
        {
            a.push_back(1);
            break;
        }
        if(a[i] < 9)
        {
            a[i]++;
            break;
        }
        else
        {
            a[i] = 0;
        }
    }
    return a;
}

vector<int> decrement(vector<int> a)
{
    for(int i = 0; i < a.size();i++)
    {
        if(i == a.size() - 1)
        {
            if(a[i] == 1 && i > 0)
            {
                a.pop_back();
            }
            else
                a[i]--;
            break;
        }
        if(a[i] > 0)
        {
            a[i]--;
            break;
        }
        else
        {
            a[i] = 9;
        }
    }
    return a;
}

bool isZero(vector<int> a)
{
    if(a.size() == 1 && a[0] == 0)
        return true;
    else
        return false;
}

vector<int> vec_square(vector<int> a)
{
    vector<int> counter1 = a;
    vector<int> result;
    result.push_back(0);
    while(!isZero(counter1))
    {
        vector<int> counter2 = a;
        while(!isZero(counter2))
        {
            result = increment(result);
            counter2 = decrement(counter2);
        }
        counter1 = decrement(counter1);
    }
    return result;
}

int vec_compare(vector<int> a, vector<int> b)
{
    //cout<<"a "<<a.size()<<endl;
    //cout<<"b "<<b.size()<<endl;
    //vec_read(b);
    if(a.size() > b.size())
        return 1;
    if(a.size() < b.size())
        return 2;
    else
    {
        for(int i = a.size() - 1; i >= 0; i--)
        {
            if(a[i] > b[i])
            {
                return 1;
            }
            if(a[i] < b[i])
            {
                return 2;
            }

        }
    }
    return 0;
}

bool is_fair(vector<int> a)
{
    int i = 0;
    int j = a.size() - 1;

    while(i < j)
    {
        if(a[i] != a[j])
            return false;
        i++;
        j--;
    }
    return true;
}

void vec_read(vector<int> a)
{
    for(int i = a.size() - 1; i >= 0;i--)
    {
        cout<<a[i];
    }
    cout<<endl;
}