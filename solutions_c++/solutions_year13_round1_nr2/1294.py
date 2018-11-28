#define DEBUG_ACTIVE
#define DEBUG_FUNCTION_ACTIVE

#ifdef DEBUG_ACTIVE
#define DEBUG(x) cout << #x << ": " << (x) << endl;
#define DO_DEBUG(x) { cout << #x << ": " << x << endl; }
#define VOID_DEBUG(x) { cout << #x << ": " << endl; x; }
#define PRINT(x) cout << (x) << endl;
#else
#define DEBUG
#define DO_DEBUG
#define VOID_DEBUG
#define PRINT
#endif

#ifdef DEBUG_FUNCTION_ACTIVE
int level = 0;
#define IN_FUNCTION level++;
#define OUT_FUNCTION level--;
#define FUNCTION for (int i = 0; i<level; i++) cout << " "; cout << "function: " << __FUNCTION__ << endl;
#define IF(x) DEBUG(x) if(x)
#define WHILE(x) DEBUG(x); while(x)
#else
#define IN_FUNCTION
#define OUT_FUNCTION
#define FUNCTION
#define IF if
#define WHILE while
#endif