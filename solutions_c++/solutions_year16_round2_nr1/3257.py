    #include<iostream>
    #include<vector>
    #include <algorithm>
    #include <fstream>
    
    using namespace std;
    int main()
    {
    	ofstream cout( "output1.txt");
    	ifstream cin( "input1.txt");
    	ios::sync_with_stdio(false);
    	int t;
    	cin>>t;
    	for(int p=1;p<=t;p++)
    	{
    		string s;
    		cin>>s;
    		int a[91]={0};
    		int n[2000];
    		for(int i=0;i<2000;i++)
    			n[i]=-1;
    		for(int i=0;i<s.size();i++)
    			a[s[i]]++;
    		int count=s.size();
    		int k=0,j=0;
    		while(count)
    		{
    			if(a['Z'])
    			{
    				n[k++]=0;
    				a['Z']--;a['E']--;a['R']--;a['O']--;
    				count-=4;
    				j++;
    			}
     
    			else if(a['W'])
    			{
    				n[k++]=2;
    				a['O']--;a['T']--;a['W']--;
    				count-=3;j++;
    			}
    			else if(a['U'])
    			{
    				n[k++]=4;
    				a['O']--;a['F']--;a['U']--;a['R'];
    				count-=4;j++;
    			}
    			else if(a['X'])
    			{
    				n[k++]=6;
    				a['S']--;a['I']--;a['X']--;
    				count-=3;j++;
    			}
    			else if(a['G'])
    			{
    				n[k++]=8;
    				a['I']--;a['E']--;a['G']--;a['H']--;a['T']--;
    				count-=5;j++;
    			}
    			else if(a['F'] && a['V'])
    			{
    				n[k++]=5;
    				a['F']--;a['E']--;a['I']--;a['V'];
    				count-=4;j++;
    			}
    			else if(a['H'] && a['R'] && a['T'] && a['E']>=2)
    			{
    				n[k++]=3;
    				a['H']--;a['T']--;a['R']--;a['E']--;a['E']--;
    				count-=5;j++;
    			}
    			else if(a['S'] && a['V'] && a['E']>=2 && a['N'])
    			{
    				n[k++]=7;
    				a['S']--;a['E']--;a['V']--;a['E']--;a['N']--;
    				count-=5;j++;
    			}
    			else if(a['N'] && a['I'])
    			{
    				n[k++]=9;
    				a['N']--;a['I']--;a['N']--;a['E']--;
    				count-=4;j++;
    			}
    			else
    			{
    				n[k++]=1;
    				a['O']--;a['N']--;a['E']--;
    				count-=3;j++;
    			}
    		}
    		int i=0;
    		vector <int> result;
    		for( int k = 0 ; k < j ; k++ ){
    			result.push_back( n[k] );
			}
			
			sort( result.begin() , result.end() );
    		cout<<"Case #"<<p<<": ";
    		while(j)
    		{
    			cout<<result[i];
    			i++;j--;
    		}
    		cout<<"\n";
    	}
    	return 0;
    }
