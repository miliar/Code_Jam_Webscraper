#include <bits/stdc++.h>
using namespace std;
 
int ans,ans2,k,n;
	vector<string> word;

typedef struct Node{
	int n;
	char c;	
	struct Node *child[26];
}node;

typedef struct Trie{
	node *root;
}trie;

int clearnode(node *n){
	int i,ans=0;
	for( i=0 ; i<26 ; i++ ) if(n->child[i]!=NULL) ans+=clearnode(n->child[i]);
	free(n);
	return 1+ans;
}
int clear(trie *t){
	return clearnode(t->root);
}

node* newnode(){
	node *temp = (node*)malloc(sizeof(node));
	temp->n = temp->c = 0;
	int i;
	for( i=0 ; i<26 ; i++ ){
		temp->child[i]=NULL;
	}
	return temp;
}

void insert(trie *t,const char word[]){
	node *temp = t->root;
	int i;
	
	for( i=0 ; word[i] ; i++ ){
		if( temp->child[word[i]-'A']==NULL ){
			temp->child[word[i]-'A']=newnode();
		}
		temp = temp->child[word[i]-'A'];
		temp->n++;
		temp->c = word[i];
		if( temp->n <=k ) ans++;
	}
}

void insert2(trie *t,const char word[]){
	node *temp = t->root;
	int i;
	
	for( i=0 ; word[i] ; i++ ){
		if( temp->child[word[i]-'A']==NULL ){
			temp->child[word[i]-'A']=newnode();
		}
		temp = temp->child[word[i]-'A'];
		temp->n++;
		temp->c = word[i];
	}
}

typedef struct State{
	int size;
	vector<int> sets[5];
}state;

int calc(int depth,state s){
	if( depth==n ){	// done
		int now=0;
		for( int i=0 ; i<s.size ; i++ ){
			trie t;
			t.root = newnode();
			for( int j=0 ; j<s.sets[i].size() ; j++ ){
				insert2(&t,word[s.sets[i][j]].c_str());
			}
			int temp = clear(&t);
			
			if( temp>1 ) now+=temp;
		}
		if( now==ans ) ans2++;
	}
	else{
		for( int i=0 ; i<k ; i++ ){
			s.sets[i].push_back(depth);
			calc(depth+1,s);
			s.sets[i].pop_back();
		}
	}
}

int main(){

	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int test,i,j,tc=1,temp;
	char in[15];
	trie t;
	
	for( scanf("%d",&test) ; test-- ; printf("Case #%d: %d %d\n",tc++,ans,ans2) ){
		scanf("%d%d",&n,&k);
		ans=ans2=0;
		word.clear();
		t.root= newnode();
		for( i=0 ; i<n ; i++ ){
			scanf("%s",in);
			word.push_back(in);
			insert(&t,in);
		}
		
		ans+=k;
		
		state s;
		s.size=k;
		calc(0,s);		
		
		clear(&t);
	}
	
	return 0;
}

